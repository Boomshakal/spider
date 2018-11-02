from lxml import etree
import requests
import json

url="http://eip.megmeet.com:8008/sys/task/sys_task_main/sysTaskIndex.do?"
maxpage=5
headers={

    "Cookie": "j_lang=zh-CN; JSESSIONID=A03ACE72F5C69DE72FB4A7AB78C8C420",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

def get_onepage(page):
    data = {
        "method": "list",
        "q.mydoc": "all",
        "q.j_path": "/listAll",
        "q.s_raq": "0.6779489634474305",
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
