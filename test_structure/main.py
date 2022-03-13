
from unittest import result
import modules.config_handler as ConfigHandler
import modules.ssh_client as SshHandler
import modules.test_handler as TestHandler
import modules.result_handler as ResultHandler

config = None
ssh = None
tester = None
resulter = None

def init_modules():
    global config, ssh, tester, resulter
    try:
        config = ConfigHandler.ConfigHandler("config.json")
        ssh = SshHandler.SshHandler(config)
        tester = TestHandler.TestHandler(ssh)
        resulter = ResultHandler.ResultHandler(config.get_param("results")["save_as"])
    except Exception as error:
        raise Exception (error)


def main():
    try:
        init_modules()
        resulter.open_file(config.get_param("results")["path"])
        tester.test_commands(config.get_param("commands"))
        resulter.save_results(tester.get_results())
        resulter.close_file()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()