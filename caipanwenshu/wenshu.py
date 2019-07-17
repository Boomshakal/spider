import requests
import os
import execjs

url = 'http://wenshu.court.gov.cn/List/ListContent',
path = os.path.abspath('.')

with open(path + '/裁判文书.js', 'r', encoding='utf-8') as f:
    js = f.read()

vl5x = execjs.compile(js).call('getKey')
guid = execjs.compile(js).call('getguid')

datas = {
    'Param': '案件类型:行政案件',
    'Index': '1',
    'Page': '10',
    'Order': '法院层级',
    'Direction': 'asc',
    'vl5x': vl5x,
    'number': 'wens',
    'guid': guid,
}

headers = {
    'Host': 'wenshu.court.gov.cn',
    'Origin': 'http://wenshu.court.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1++%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6+%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E8%A1%8C%E6%94%BF%E6%A1%88%E4%BB%B6',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': '_gscu_2116842793=62375526zgldxm14; _gscbrs_2116842793=1; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1562375527; VCode=b8f147a5-8b5e-4067-99b9-e357c2749703; User=UserName=2047114221@qq.com&RoleName=0; AutoLogin=UserName=2047114221@qq.com&Pwd=824B8E0CFBB2335F12EA262A7F0B0424&IsAutoLogin=1; R=v=2047114221@qq.com_1e773113-8dfa-4bf7-b8a8-3963f211b7b4|122.226.143.230; _gscs_2116842793=t62382023xgslho21|pv:6; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1562383575; vjkl5=f59994ff51c5610169185d26b3de9c9093069f4d'
}

results = requests.post(url=url, data=datas, headers=headers)


print(results)
