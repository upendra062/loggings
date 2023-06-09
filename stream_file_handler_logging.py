import logging

# create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('abc.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# create formatters and add it to handler

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add Handler to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


logger.warning('this is a Warning')
logger.error('This is error')