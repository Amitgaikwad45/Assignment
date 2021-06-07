import logging

logging.basicConfig(filename="C:/Users/Amit/PycharmProjects/POM_pytest/venv/Scripts/test.log",format='%(asctime)s: %(levelname)s: %(message)s',

                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning")
logging.error("error message")
logging.critical("critical message")
