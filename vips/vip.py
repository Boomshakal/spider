import re
import json
import  requests

url='https://category.vip.com/suggest.php?keyword=%E6%89%8B%E6%9C%BA&page=3&count=50&suggestType=brand#catPerPos'

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
rsp = requests.get(url=url,headers=headers)
# print(rsp.text)
result = re.findall('"products":\[.*?\]',rsp.text,re.S)[0]
print(type(result))


# json = json.loads(result)
#
# print(json['price_info'])