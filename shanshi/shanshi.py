import json

import requests

url = 'http://oa.tzle1.com:81/api/Orders/bx_change_moneyfromemail'
data = {
    'baoxiu_order_ordernum': 'DDFB2021020100155'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
res = requests.post(url, data=data, headers=headers)
print(res.text)
# res_dic = json.loads(res.text)
#
# photo = res_dic['order_confirm_info']['confirm_before_url']
# video = res_dic['order_confirm_info']['confirm_txm_url']
#
# print(photo,video)