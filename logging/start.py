import sys
import logging
import logging.handlers


root = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s','%m/%d/%Y %I:%M:%S %p')
ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(filename="/home/rijumone/Kitchen/python/logging/log.log", maxBytes=1024*1, backupCount=9)

handler.setFormatter(formatter)
root.addHandler(handler)
root.addHandler(ch)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
