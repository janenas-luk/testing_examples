

class TestHandler:

    __connection = None
    __results = []

    def __init__(self, connection):
        self.__connection = connection

    def test_commands(self, commands):
        for command in commands:
            result = {}
            response = self.test_command(command["command"], command["expects"])
            result["command"] = command["command"]
            result["expects"] = command["expects"]
            result["status"] = response
            self.__results.append(result)

    def test_command(self, command, expects):
        response = self.__connection.exec_command(command)
        if response == expects:
            return "Passed"
        else:
            return "Failed"
    
    def get_results(self):
        return self.__results