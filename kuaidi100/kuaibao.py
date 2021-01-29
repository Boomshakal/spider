import hashlib
import json
import time

import requests

url = 'https://kop.kuaidihelp.com/api'

appId = '''106611'''
method = '''express.info.get'''
ts = int(time.time())
appKey = '''c9277da6014e6d40c5e9b31a649ba710984ac9bc'''

print(str(ts))
signStr = appId + method + str(ts) + appKey
sign = hashlib.md5(signStr.encode('utf8')).hexdigest()

data = {
    'app_id': appId,
    'method': method,
    'ts': str(ts),
    'sign': sign,
    'data': '''{
        "waybill_no": "4306923169630",
        "exp_company_code": "yd",
        "result_sort": "0"
    }
    '''
}

headers = {
    'content-type': "application/x-www-form-urlencoded",
}

res = requests.post(url, data=data, headers=headers)
res_dic = json.loads(res.text)
# print(res_dic)
for data in res_dic.get('data')[0].get('data'):
    print(data)
