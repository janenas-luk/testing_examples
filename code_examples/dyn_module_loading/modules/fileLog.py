
class loggerCon:

    __logFile = None

    def open_log(self, file):
        if not file:
            file = "/home/janenaslu/logger.log"
        try:
            log = open(file, "a+")
            self.__logFile = log
        except:
            print("Error")

    def close_log(self):
        if self.__logFile:
            self.__logFile.close()

    def write_to_log(self, level, message, timestamp):
        data = "%s,%s,%s\n"%(str(timestamp), str(level), message)
        self.__logFile.write(data)



# log = logger()
# log.write_to_log(1, "Some text", time.time())

