import logging

logging.basicConfig(filename= 'logs.log', level= logging.DEBUG, format='%(asctime)s %(message)s')

def logError(errorMessage):
    logging.error(errorMessage)