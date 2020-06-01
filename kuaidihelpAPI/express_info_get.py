import time
import requests
import hashlib

url = 'https://kop.kuaidihelp.com/api'

appId = '''106611'''
method = '''express.info.get'''
ts = int(time.time())
appKey = '''c9277da6014e6d40c5e9b31a649ba710984ac9bc'''

# // 计算签名
signStr = appId + method + str(ts) + appKey
sign = hashlib.md5(signStr.encode('utf8')).hexdigest()

payload_list = {}
payload_list['app_id'] = appId
payload_list['method'] = method
payload_list['ts'] = str(ts)
payload_list['sign'] = sign
payload_list['data'] = '''{ "waybill_no":"1100435729150", "exp_company_code":"ems","result_sort":"0"}'''

headers = {
    'content-type': "application/x-www-form-urlencoded",
}

res = requests.post(url=url, data=payload_list, headers=headers)
print(res.text)
