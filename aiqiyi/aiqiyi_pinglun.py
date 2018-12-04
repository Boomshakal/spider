import json

import requests

for page in range(1,4):
    url='https://sns-comment.iqiyi.com/v3/comment/get_comments.action?'
    params={
            'agent_type': 118,
            'agent_version': '9.11.5',
            'authcookie': 'null',
            'business_type': 17,
            'content_id': 1629260900,
            'hot_size': 0,
            'last_id': '',
            'page': page,
            'page_size': 20,
            'types': 'time',
            #'callback': 'jsonp_1543836570490_3918'
    }
    rsp=requests.get(url=url,params=params).text
    data=json.loads(rsp)['data']['comments']
    for j in data:

        print(j['content'])