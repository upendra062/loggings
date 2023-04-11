import logging
import saveToFile as STF

####--------------------------------------------------------------
#### created our own logger This is called customizing
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

fh = logging.FileHandler('employee.log')
fh.setFormatter(f)  

logger.addHandler(fh)
####--------------------------------------------------------------



# logging.basicConfig(filename='employee.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# logging.debug('Start of employee program')

logger.debug('Start of employee program')
name = 'upendra singh bhadauria'
age = 24
email = 'bhadauriaupendra062@gmail.com'

if STF.namecheck(name) is True:
    STF.saveData(name, age, email)
else:
    logger.critical('Employee check failed')

logger.debug("End of employee program")
logger.debug("###########################")