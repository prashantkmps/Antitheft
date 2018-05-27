import paramiko


def execute_command_remotely(hostname, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())
    ssh.close()
