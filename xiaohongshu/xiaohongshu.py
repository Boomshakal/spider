import json

import requests

url = 'https://www.xiaohongshu.com/wx_mp_api/sns/v1/homefeed?oid=recommend&page=25&page_size=20'

headers = {
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}

result =requests.get(url=url,headers=headers)
datas = json.loads(result.text)['data']
for data in datas:
    print(data['id'])
