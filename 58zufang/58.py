import re

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib import request, parse
from http import cookiejar
from fontTools.ttLib import TTFont


#  创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    login_url = "https://passport.58.com/58/login/pc/dologin"
    # 此login_url需要从登录form的action属性中提取
    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "username": "15168633879",
        "password": "lhm922357"
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(login_url, data=bytes(data,encoding='utf-8'))
    # 使用opener发起请求
    response = opener.open(req)

def get_response():
    url='https://tz.58.com/chuzu/?PGTID=0d3090a7-0019-3300-4402-c37bdfa0779a'
    rsp = opener.open(url)
    html = rsp.read().decode()
    print(html)
    return html


def parse_font():
    font1 = TTFont('58tc.woff')
    print(font1.getBestCmap())
    keys, values = [], []
    #dict = {}
    for k, v in font1.getBestCmap().items():
        if v.startswith('uni'):
            keys.append(eval("u'\\u{}".format(k) + "'"))
            values.append(chr(int(v[3:], 16)))
        else:
            keys.append("&#x{}".format(k))
            values.append(v)
    # for i,j in zip(keys,values):
    #     dict[i] =j
    #print(dict)
    return keys, values




if __name__ == '__main__':
    #login()
    response=get_response()
    # font_url = re.findall(r'src:url\((.*?)\)', response, re.S)[0]
    # # print(font_url[1:-1])
    # urlretrieve(font_url[1:-1], '58tz.woff')
    #
    # soup = BeautifulSoup(response, 'html.parser')
    # datas = soup.find_all('ul',class_='listUl')
    #
    # for date in datas:
    #     title = str(date.text).strip()
    #     # keys, values = parse_font()
    #     # for k, v in zip(keys, values):
    #     #     title = title.replace(k, v)
    #     print(title)
    parse_font()
