from .log import server_logger, log_path, get_log, get_log_recent
import logging
from os.path import exists


# create file if not exists
if not exists(log_path):
    with open(log_path, 'w') as f:
        pass

# create file handler
fh = logging.FileHandler(log_path)
fh.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to file handler
fh.setFormatter(formatter)

# add file handler to logger
server_logger.addHandler(fh)

# set logger level (need to do this as well as file handler level!)
server_logger.setLevel(logging.INFO)