#!/usr/bin/env python3
"""Atlassian Confluence Update

Script to regex replace stuff on confluence pages.
"""
import logging
import sys
from getpass import getpass
import regex
from atlassian import Confluence
from atlassian.errors import ApiPermissionError

log_level = logging.INFO

confluence_server = input('Enter confluence server url (without protocol): ')
confluence_user = input('Please enter confluence user name: ')
confluence_password = getpass(f'Please enter Confluence password for user {confluence_user}: ')


def confluence_connect(conf_server, conf_user, conf_password):
    """Connect to confluence server and check success

    :param conf_server server url (without https)
    :param conf_user user name for confluence
    :param conf_password password for confluence user
    :return: confluence connection object
    """
    try:
        logging.info('Connecting to Confluence (%s)...', confluence_server)
        conn = Confluence(url=f'https://{confluence_server}', username=confluence_user, password=confluence_password)
        # atlassian API does not raise an exception on failed login, so manual workaround to do this
        try:
            conn.get_user_details_by_username(confluence_user, expand=None)
        except ApiPermissionError as err:
            raise PermissionError('Permission error: Login failed.') from err
        return conn

    except Exception as err:
        logging.error('  ... failed to connect to Confluence.')
        logging.error(err)
        sys.exit()

def confluence_site_search(conf_connection, query_str, q_type=None, q_space=None, limit=None):
    """Search confluence using query_string.

    :param conf_connection confluence connection object
    :param query_str query string
    :return: list of confluence page IDs that are hits for the query string
    :rtype: list
    """
    try:
        cql = 'siteSearch ~ "' + query_str+ '"'
        if q_type:
            cql = cql + ' and type="' + q_type + '"'
        if q_space:
            cql = cql + ' and space="' + q_space + '"'
        logging.info('Sending CQL search query \'%s\'...', cql)
        search_results = conf_connection.cql(cql,limit=limit)
        id_list = [result['content']['id'] for result in search_results['results']]
        logging.info(' ... %s records found.', len(id_list))
        return id_list

    except Exception as err:
        logging.error('  ... failed to complete query.')
        return None

def update_confluence_pages(conf_connection, page_id_list, search_pattern, replace_pattern, commit_msg=None):
    """Regex replace pattern in all pages in page_ids_list.

    :param conf_connection confluence connection object
    :param page_id_list list of confluence page ids
    :param search_pattern regex search pattern string
    :param replace_pattern regex replacement string
    :return:
    :rtype:
    """
    rex = regex.compile(search_pattern)
    logging.info('Search pattern is %s', search_pattern)
    logging.info('Replacement pattern is %s', replace_pattern)

    for pid in page_id_list:
        logging.info('Editing page %s ...', pid)
        page = conf_connection.get_page_by_id(pid, expand='body.storage,version')
        page_title = page['title']
        logging.info('  ... page title: %s', page_title)
        page_body = page['body']['storage']['value']
        page_body, num = rex.subn(replace_pattern, page_body)
        logging.info('  ... number of replacements: %s', num)

        conf_connection.update_page(pid, page_title, page_body, version_comment=commit_msg)

def main():
    """Main function.
    """
    # connect to server
    conf = confluence_connect(confluence_server, confluence_user, confluence_password)

    # if find_limit is not set, search results seem to be limited to 25?
    find_limit = 1000

    # space and type can be None, then all spaces/types will be included
    page_space = None
    page_type = 'page'

    # confluence search allows wildcards * (multiple chars) and ? (single char) EXCEPT at the very beginning!
    query_string = 'TESTSTRINGFORTESTING*'

    # regex pattern
    search_pattern = 'TESTSTRINGFORTESTING'
    replace_pattern = 'TESTSTRINGFORTESTINGNEWLYREPLACED'

    # set confluence 
    commit_message = f'{__file__}: Bulk regex replacement of pattern "{search_pattern}" with "{replace_pattern}"'

    # find pages
    page_ids = confluence_site_search(conf, query_string, page_type, page_space, find_limit)
    logging.info(page_ids)

    # update pages
    update_confluence_pages(conf, page_ids, search_pattern, replace_pattern, commit_message)

if __name__ == "__main__":
    main()
