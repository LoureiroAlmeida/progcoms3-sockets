import logging

# add filemode="w" to overwrite
#logging.basicConfig(filename="log/sample.log", level=logging.INFO)
#logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")