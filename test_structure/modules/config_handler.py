import os
import json

class ConfigHandler:

    __config = None
    __error = None

    def __init__(self, configPath="config.json"):
        if not self.__load_config(configPath):
            raise Exception(self.__error)

    def __load_config(self, configPath):
        if not os.path.exists(configPath):
            self.__error = "Config file does not exists"
            return None
        config = open(configPath, "r")
        content = config.read()
        if not self.__is_json(content):
            self.__error = "Config file content is not JSON"
            return None
        self.__config = json.loads(content)
        config.close()
        return True

    def __is_json(self, content):
        try:
            json.loads(content)
        except:
            return False
        return True

    def get_param(self, param):
        if param in self.__config.keys():
            return self.__config[param]
        else:
            return None