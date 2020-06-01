import http.client , urllib, hashlib
import time

conn = http.client.HTTPSConnection("kop.kuaidihelp.com")

appId = '''106611'''
method = '''cloud.address.resolve'''
ts = int(time.time())
appKey = '''c9277da6014e6d40c5e9b31a649ba710984ac9bc'''

# // 计算签名
signStr = appId + method + str(ts) + appKey
sign = hashlib.md5(signStr.encode('utf8')).hexdigest()

payload_list={}
payload_list['app_id']=appId
payload_list['method']=method
payload_list['ts']=str(ts)
payload_list['sign']=sign
payload_list['data']='''{
    "text":"浙江省绍兴市诸暨市浣东街道西子公寓北区电话：13905857430  衣服  食物 ",
    "multimode":false
}'''

payload =urllib.parse.urlencode(payload_list)
headers = {
    'content-type': "application/x-www-form-urlencoded",
    }

conn.request("POST", "/api", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))