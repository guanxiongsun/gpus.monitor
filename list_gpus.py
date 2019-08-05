import yaml
import paramiko
from easydict import EasyDict

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--server_list', default='server_list.yaml',
                    help='list of servers')
parser.add_argument('--user', default='',
                    help='username of all servers')
parser.add_argument('--password', default='',
                    help='password of user on all servers')


def main(config=None):
    client_list = []

    for _, server in config.items():
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server.host, username=server.user, password=server.password)
        client_list.append(client)

    for client in client_list:
        stdin, stdout, stderr = client.exec_command('gpustat')
        for line in stdout:
            print(line.strip('\n'))
        client.close()


if __name__ == '__main__':
    args = parser.parse_args()

    with open(args.server_list) as f:
        config = yaml.load(f)

    config = EasyDict(config['servers'])

    if args.user:
        for key, server in config.items():
            server.update({'user': args.user})
            server.update({'password': args.password})

    main(config)

