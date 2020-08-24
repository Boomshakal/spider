import base64
import hashlib
import time

import requests

HOST = 'https://apis.7moor.com'
ACCOUNTID = 'N00000048930'
APISecret = '08f227c0-8781-11ea-a93c-c76583ff8e29'

url_base = '{HOST}/v20180426/report/getReportData/{ACCOUNTID}?sig={SIG}'

now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
auth_base = ACCOUNTID + ':' + now

auth = base64.b64encode(auth_base.encode('utf-8')).decode()
headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': auth,
}

sig_base = ACCOUNTID + APISecret + now
sig = hashlib.md5(sig_base.encode('utf-8')).hexdigest().upper()

url = url_base.format(HOST=HOST, ACCOUNTID=ACCOUNTID, SIG=sig)
print(url)

data = {
    'reportType': 'call_report_agent',
    'yearReport': '2020',
    'monthReport': '07',
    # 'dayReport':'',
    'timeType': 'month'
}
res = requests.post(url=url, json=data, headers=headers)


print(res.text)