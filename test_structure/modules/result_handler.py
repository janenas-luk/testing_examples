
class ResultHandler:

    __resultSaver = None

    def __init__(self, type):
        self.__resultSaver = self.__load_module(type)
        if not self.__resultSaver:
            raise Exception("Unable to load result handler module")

    def __load_module(self, type):
        module = None
        try:
            module = __import__('modules.{type}_saver'.format(type=type), fromlist=['modules'])
            return module.ResultSaver()
        except:
            return False

    def open_file(self, path):
        self.__resultSaver.open_file(path)

    def close_file(self):
        self.__resultSaver.close_file()

    def save_results(self, results):
        self.__resultSaver.save_results(results)