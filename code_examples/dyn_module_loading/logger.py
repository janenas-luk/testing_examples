import time

class logger:

    __logger = None

    def __init__(self, conType):
        self.__logger = self.__load_module(conType)
        if not self.__logger:
            exit("Unable to load logger")

    def __load_module(self, conType):
        module = None
        try:
            module = __import__('modules.{type}Log'.format(type=conType), fromlist=['modules'])
            return module.loggerCon()
        except:
            return False

    def open_log(self, file):
        self.__logger.open_log(file)

    def close_log(self):
        self.__logger.close_log()

    def write_to_log(self, level, message, timestamp):
        self.__logger.write_to_log(level, message, timestamp)
        

# log = logger("sqlite")
log = logger("file")
log.open_log(None)
log.write_to_log(0, "Info message", time.time())
log.write_to_log(1, "Warning message", time.time())
log.write_to_log(2, "Error message", time.time())
log.close_log()

