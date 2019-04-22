import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
from fontTools.ttLib import TTFont


def get_response():
    url = 'https://m.58.com/gz/qzyewu/pn1/?reform=pcfront'
    headers = {
        'authority': 'm.58.com',
        'method': 'GET',
        'path': '/gz/qzyewu/pn2/?reform=pcfront&PGTID=0d303353-0000-3f36-e12a-3e4c239050a4&ClickID=2&segment=true',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'f=n; id58=c5/njVw1zDFsj83TBA4MAg==; 58tj_uuid=10c6879a-760b-4754-afa1-0fb1f5b0fc12; als=0; __utma=253535702.1877351784.1547029555.1547029555.1548918015.2; __utmz=253535702.1548918015.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; city=sh; 58home=sh; wmda_uuid=5bcd52e27e1ca928a262958ae23846fe; wmda_new_uuid=1; wmda_visited_projects=%3B2385390625025; xxzl_deviceid=kaWnkw7KX8T2RCmSUWyrSm0%2BRTaHxr7dklX5it5enKJyoVP3jXCTPPbcNlqeMk7p; sessionid=a63b2622-6788-4db5-bfaf-836bf3b60c74; device=m; new_uv=4; qz_gdt=; utm_source=; spm=; init_refer=; scancat=13139; Hm_lvt_35e5bfb064bb1db376f3263abb7cfe79=1555137939; m58comvp=t13v115.159.229.24; hasLaunchPage=%7Cl_searchjob_qzyewu%7C; launchFlag=1; Hm_lvt_fb84137acd0fd92ca74ea0f89f207b1f=1555137939; f=n; new_session=0; cookieshow_13139=11; ppStore_fingerprint=96D8AAFDAD9596640390B38637943FB0CF146BCB8CD892C3%EF%BC%BF1555138230467; Hm_lpvt_35e5bfb064bb1db376f3263abb7cfe79=1555138232; Hm_lpvt_fb84137acd0fd92ca74ea0f89f207b1f=1555138233; JSESSIONID=2D33CDB828683462B5850797534E140F',
        'referer': 'https://m.58.com/gz/qzyewu/pn1/?reform=pcfront&PGTID=0d303353-0000-3f36-e12a-3e4c239050a4&ClickID=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    return response


# 解析字体文件 ，获取相应的字体映射关系
def parse_font():
    font1 = TTFont('58tc.woff')
    keys, values = [], []
    #dict = {}
    for k, v in font1.getBestCmap().items():
        if v.startswith('uni'):
            keys.append(eval("u'\\u{:x}".format(k) + "'"))
            values.append(chr(int(v[3:], 16)))
        else:
            keys.append("&#x{:x}".format(k))
            values.append(v)
    # for i,j in zip(keys,values):
    #     dict[i] =j
    #print(dict)
    return keys, values


# 获取数据并对特殊字体转码
def get_data():
    # 获取内容
    response = get_response()
    # 获取woff文件
    font_url = re.findall(r'src:url\((.*?)\)', response.text, re.S)[0]
    print(type(font_url))
    urlretrieve(font_url, '58tc.woff')

    # 解析内容
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.findAll('dt',class_='tit')
    for info in data:
        title = str(info.text).strip()
        keys, values = parse_font()
        for k, v in zip(keys, values):
            title = title.replace(k, v)
        print(title)

    # url = soup.find_all()
    # for a in url:
    #     #if a['href'].startswith('//jianli'):
    #     print(a)

if __name__ == '__main__':
    get_data()
