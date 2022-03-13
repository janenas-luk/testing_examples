import paramiko

class SshHandler:

    __ssh_client = None

    def __init__(self, config):
        addr = config.get_param("address")
        username = config.get_param("username")
        password = config.get_param("password")
        if not self.__open_connection(addr, username, password):
            raise Exception("Unable to connect to SSH server")

    def __close_connection(self):
        if self.__ssh_client:
            self.__ssh_client.close()

    def __open_connection(self, addr, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(addr, 22, username, password)
            self.__ssh_client = client
            return True
        except:
            return None

    def exec_command(self, command):
        success = True
        stdin, stdout, stderr = self.__ssh_client.exec_command(command)
        # print(''.join(stderr.readlines()))
        if stderr.readlines():
            success = False
        return success

    def __del__(self):
        self.__close_connection()