from atlassian import Confluence
from atlassian.errors import ApiPermissionError

confluence_server = ''
confluence_user = ''
confluence_password = ''


def confluence_connect(confluence_server, confluence_user, confluence_password):
    try: 
        c = Confluence(url=confluence_server, username=confluence_user, password=confluence_password)
        # atlassian API does not raise an exception on failed login, so manual workaround to do this     
        try:
            c.get_user_details_by_username(confluence_user, expand=None)
        except ApiPermissionError as err:
            raise PermissionError('Permission error: Login failed.') from err
        print('success!')
        return c

    except Exception as e:
        print('  ... failed to connect to Confluence.')

def confluence_site_search(conf_connection, query, q_type=None, q_space=None, limit=None):
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
