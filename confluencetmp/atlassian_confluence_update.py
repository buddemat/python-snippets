from atlassian import Confluence
from atlassian.errors import ApiPermissionError

confluence_server = ''
confluence_user = ''
confluence_password = ''

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

