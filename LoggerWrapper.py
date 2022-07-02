import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename= f'{dir_path}/logs.log', level= logging.DEBUG, format='%(asctime)s %(message)s')

def logError(errorMessage):
    logging.error(errorMessage)
