import logging
import yaml
from pathlib import Path


# Load options 
options = yaml.safe_load(open('./config.yml'))

# Initialize logging
log_file_name = options.get('logging').get('filename')
if not log_file_name:
    log_file_name = f'{Path(__file__).stem}.log'
logger = logging.getLogger('mylogger')
log_file_handler = logging.FileHandler(filename = log_file_name, 
                                       encoding = 'utf-8', 
                                       mode = 'w')

if options.get('logging').get('stdout'):
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
