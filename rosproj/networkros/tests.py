from django.test import TestCase

# Create your tests here.

# from librouteros import connect
# import json
# user = 'zhaoping'
# password = 'KingJuniper'
# host= '223.167.134.180'
# api = connect(username=user, password=password, host=host,port= 18728)
# info = api(cmd='add/name={}/password={}/service= l2tp/profile=default'.format('user2','user2'))
# info2 = api(cmd='/ppp/secret/print')
# for i in info2:
#     print(i)
# print(json.dumps(ip_info,indent=4,sort_keys=True))
# for i in info:
#     print(i)

import paramiko
def ros(name,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname='223.167.134.180', port=18730,
                    username='zhaoping', password='KingJuniper',
                    look_for_keys=False)
    except Exception as error:
        print(error)
        return
    else:
        command = '/ppp secret add name={} password={} service= l2tp profile=default'.format(name,password)
        _, stdout, _ = ssh.exec_command(command)
        _, stdout, _ = ssh.exec_command('/ppp secret print')
        res = stdout.read()
        print(str(res,'utf-8'))
ros('user3','user3')


