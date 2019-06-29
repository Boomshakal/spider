import base64

import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
from fontTools.ttLib import TTFont, BytesIO


def get_response():
    url = 'https://hz.58.com/qzduomeiti/?PGTID=0d3097aa-0004-f673-21c0-6fbdffab6d74&ClickID=3'
    headers = {
        'authority': 'hz.58.com',
        'method': 'GET',
        'path': '/qzduomeiti/?PGTID=0d3097aa-0004-f673-21c0-6fbdffab6d74&ClickID=3',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=tz%7C%E5%8F%B0%E5%B7%9E%7C0; id58=c5/njVylusRD/R7DAz/jAg==; 58tj_uuid=963b07e8-f471-4541-a262-b0726c9db6de; als=0; wmda_uuid=526920c89ff21cf2e8c4757ec0818d33; wmda_new_uuid=1; wmda_visited_projects=%3B1731916484865; xxzl_deviceid=g2ro0VR4jiHN9iOqeWu0NNZors9nQKm%2F9aaJTkiUQsD0o3zS25M6WY5RwWfmWuRd; param8616=1; param8716kop=1; isSmartSortTipShowed=true; cookieuid1=mgjwFVy0Kgs/jDhpFqgnAg==; 58home=tz; city=tz; gr_user_id=26811053-0c37-4dca-91ca-510376d4328c; show_zcm_banner=true; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253D4TKtUE7L8cDJ3ZA8sidrCXKu-IV__OzCScWpB8MqIyy%2526wd%253D%2526eqid%253Dc1b5c9c30002acb4000000065d00ed6b; new_session=0; wmda_session_id_1731916484865=1560341888602-ef0adbc8-47ad-1584; sessionid=163e2ffd-9a40-4455-a89f-f8de103e3019; gr_session_id_b4113ecf7096b7d6=18e3e0f0-8a2b-4b56-a04b-c6c2b288d2d1; gr_session_id_b4113ecf7096b7d6_18e3e0f0-8a2b-4b56-a04b-c6c2b288d2d1=true; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1560342151; f=n; ppStore_fingerprint=118714FB1D223CDC6517CAAC5FC7ECDD8A16A67F9825B9FD%EF%BC%BF1560342184683; crmvip=""; dk_cookie=""; PPU="UID=62789580439050&UN=mur8bxx73&TT=3d326078f559ab8a823815c4ad4066c1&PBODY=T-1DDAUYuattgFQgLbb22vQQjCYWddAV61dcbYz33tapuuMSq5l8E2OsixnJ70mWMEYkYVe4GRCQO-xQs788ZeYOXdvR5pMcoL6XvTP0bOBBQKFFJba8JRA3cFwjQxdkp1RUYU4m3QtKrxGRJVJ1VdjBztmTyH4ak3Y1g3k7pvc&VER=1"; www58com="UserID=62789580439050&UserName=mur8bxx73"; 58cooper="userid=62789580439050&username=mur8bxx73"; 58uname=mur8bxx73; JSESSIONID=6725CBA8361ED997645E86345B36AF29; jl_list_left_banner=4; Hm_lpvt_a3013634de7e7a5d307653e15a0584cf=1560342247; xxzl_smartid=b0e3c9d423c5112d40d51f2b855b9413',
        'referer': 'https://hz.58.com/qzzpmeishu/pn2/?PGTID=0d3097aa-0004-fb3f-3878-70d32dd72510&ClickID=6',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    return response


# 解析字体文件 ，获取相应的字体映射关系
def parse_font():
    font1 = TTFont('58hz.woff')
    keys, values = [], []
    # dict = {}
    # print(font1.getBestCmap().items())
    for k, v in font1.getBestCmap().items():
        if v.startswith('uni'):
            keys.append("&#x{:x}".format(k))
            values.append(str(v))
        else:
            keys.append(str(k))
            values.append(str(v))

    # for i,j in zip(keys,values):
    #     dict[i] =j
    # print(dict)
    return keys, values

# 获取数据并对特殊字体转码
def get_data():
    # 获取内容
    response = get_response()
    # 获取woff文件
    font_url = re.findall(r'src:url\((.*?)\)', response.text, re.S)[0]
    # print(type(font_url))
    urlretrieve(font_url, '58hz.woff')

    # 解析内容
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('dt', class_='w325')
    for info in data:
        title = str(info.text).strip()

        print(title)


if __name__ == '__main__':
    get_data()
    # parse_font()

