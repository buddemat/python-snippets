import logging
import yaml

# Load options 
options = yaml.safe_load(open('./config.yml'))

# Initialize logging
logger = logging.getLogger('mylogger')
log_file_handler = logging.FileHandler(filename = options.get('logging').get('filename'), 
                                       encoding = 'utf-8', 
                                       mode = 'w')

if options.get('logging').get('verbose'):
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [log_file_handler, stdout_handler]
else:
    handlers = [log_file_handler]

logging.basicConfig(
         format = '%(asctime)s %(levelname)-8s %(message)s',
         level = logging.ERROR, # root logger
         datefmt = '%Y-%m-%d %H:%M:%S',
         handlers = handlers)

logger.setLevel(logging.INFO) # mylogger
