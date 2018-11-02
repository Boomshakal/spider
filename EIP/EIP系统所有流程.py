import requests
import json
from lxml import etree

url="http://eip.megmeet.com:8008/km/review/km_review_index/kmReviewIndex.do?"
maxpage=5

headers={

    "Cookie": "j_lang=zh-CN; JSESSIONID=40ABBC9A619C5860068184B1E339BC4D",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
def get_onepage(page):
    data = {
        "method": "list",
        "q.mydoc": "all",
        "q.j_path": "/listAll",
        "q.s_raq": "0.2347883935715236",
        "pageno": page,
        "rowsize": "30",
        "orderby": "docCreateTime",
        "ordertype": "down",
        "s_ajax": "true"
    }
    text=requests.get(url,headers=headers,params=data).text
    #print(type(text),text)
    jsons=json.loads(text)
    results=jsons.get('datas')
    for result in results:
        html=result[1]['value']
        html=etree.HTML(html)
        title=html.xpath('//span/text()')
        print(title)
        #print(html)

if __name__ == '__main__':
    for page in range(1,maxpage+1):
        get_onepage(page)
        print("第{0}页加载完成！".format(page))
