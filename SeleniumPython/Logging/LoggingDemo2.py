import logging

logging.basicConfig(filename="C:/Users/Amit/PycharmProjects/POM_pytest/venv/Scripts/test.log",format='%(asctime)s: %(levelname)s: %(message)s',

                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning")
logger.error("error message")
logger.critical("critical message")