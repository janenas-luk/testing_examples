import time

class ResultSaver:

    __file = None

    def __init__(self):
        pass

    def open_file(self, path):
        if not path:
            file = "./results/" + str(time.time()) + "_test.txt"
        try:
            log = open(file, "w")
            self.__file = log
        except:
            raise Exception("Unable to open file to save results")

    def close_file(self):
        if self.__file:
            self.__file.close()

    def save_results(self, results):
        header = "Command; Expects; Status\n"
        self.__write_to_file(header)
        for result in results:
            formatedString = self.__format_string(result)
            self.__write_to_file(formatedString)


    def __write_to_file(self, string):
        self.__file.write(string)

    def __format_string(self, result):
        return result["command"] + "; " + str(result["expects"]) + "; " + result["status"] + "\n"