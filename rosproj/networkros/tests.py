from django.test import TestCase

# Create your tests here.

from librouteros import connect
import json
user = 'test'
password = 'test'
host= '213.147.134.180'
api = connect(username=user, password=password, host=host,port= 18728)
info = api(cmd="/ppp/secret/print")
# print(json.dumps(ip_info,indent=4,sort_keys=True))
for i in info:
    print(i)



