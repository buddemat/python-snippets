#!/usr/bin/env python3
"""Atlassian Confluence Update

Script to regex replace stuff on confluence pages.
"""
import logging
import sys
from getpass import getpass
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
        logging.info(f'Connecting to Confluence ({confluence_server})...')
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
    :rtype:
    """
    pass


# connect to server
conf = confluence_connect(confluence_server, confluence_user, confluence_password)

query_string = ''

# if find_limit is not set, search results seem to be limited to 25?
find_limit = 1000

# space and type can be None, then all spaces/types will be included
page_space = None
page_type = 'page'

# find pages
page_ids = confluence_site_search(conf, query_string, page_type, page_space, find_limit)
