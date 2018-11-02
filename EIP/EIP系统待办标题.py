'''
EIP获取代办标题
'''
import requests
import json
from lxml import etree

url="http://eip.megmeet.com:8008/sys/notify/sys_notify_todo/sysNotifyMainIndex.do?"
data={
    "method" : "list",
    "dataType" : "todo",
    "dType": 13,
    "fdCateId":"",
    "orderby": "fdCreateTime",
    "ordertype": "down",
    "s_ajax": "true"
}
headers={

    "Cookie": "j_lang=zh-CN; JSESSIONID=0FDC84DE0B9F856EA022E6E656FDC80C",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

text=requests.get(url,headers=headers,params=data).text
#print(type(text))
jsons=json.loads(text)
results=jsons.get('datas')
#print(results)
for result in results:
    html=result[5]['value']
    html=etree.HTML(html)
    title=html.xpath('//span/@title')
    print(title)





