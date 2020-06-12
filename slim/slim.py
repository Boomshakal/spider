from urllib.parse import urlencode
from lxml import etree

import requests

base_url = 'http://www.slimego.cn/search.html?'

q = input("请输入要搜索内容:")
params = {
    'q': q,
    'page': '1',
    'rows': '20'

}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

url = base_url + urlencode(params)
print(url)
res = requests.get(url=url, headers=headers)

# print(res.text)
html = etree.HTML(res.text)

link = html.xpath("//span[@class='link']/a/@href")


print(link)