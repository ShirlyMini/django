import logging

# logging.debug("this is a debug msg")
# logging.info("this is a info msg")
# logging.warning("this is a warning msg")
# logging.error("this is a error msg")
# logging.critical("this is a critical msg")
#
# print(logging.getLogger())

logging.basicConfig(filename="test.log",
                    format="%(asctime)s %(levelname)s %(message)s",
                    filemode="w")
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
logging.debug("this is a debug msg")
logging.info("this is a info msg")
logging.warning("this is a warning msg")
logging.error("this is a error msg")
logging.critical("this is a critical msg")