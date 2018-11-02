import csv
import json
from urllib import request, parse
from http import cookiejar
from lxml import etree

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
    login_url = "http://eip.megmeet.com:8008/j_acegi_security_check"
    # 此login_url需要从登录form的action属性中提取
    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "j_username": "yhs375",
        "j_password": "lhm9223572309"
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(login_url, data=bytes(data,encoding='utf-8'))
    # 使用opener发起请求
    response = opener.open(req)

def geterrInfo(page):
    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    url = "http://eip.megmeet.com:8008/km/review/km_review_index/kmReviewIndex.do?method=list&q.mydoc=all&q.j_path=%2FlistAll&q.fdTemplate=1666236b6b0126bbc42394e49a8ae720&q.s_raq=0.006108134566174206&pageno={}&rowsize=30&orderby=docCreateTime&ordertype=down&s_ajax=true".format(page)
    # data={
    #     'method': 'list',
    #     'q.mydoc': 'all',
    #     'q.j_path': '/listAll',
    #     'q.fdTemplate': '1666236b6b0126bbc42394e49a8ae720',
    #     'q.s_raq': 0.8223910556245086,
    #     'pageno': page,
    #     'rowsize': 30,
    #     'orderby': 'docCreateTime',
    #     'ordertype': 'down',
    #     's_ajax': True
    # }
    rsp = opener.open(url)
    html = rsp.read().decode()
    result=json.loads(html)

    with open('data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['发起人', '申请编号', '机型料号', '机型名称', '托工单号', '工单数量', '物料料号', '投入数量', '不良数量', '问题描述', '原因分析', '临时措施', '围堵措施',
             '永久措施', '效果确认','发起日期','责任人'])

        for i in  result['datas']:
            fdId=i[0]['value']   #获取fdId用于next_url的get
            docCreateTime_time=i[6]['value']

            rsp = opener.open(next_url.format(fdId))
            html = rsp.read().decode()
            info=etree.HTML(html).xpath('//div[@class="xform_inputText"]//text()')
            info.append(docCreateTime_time)
            #responsibility = etree.HTML(html).xpath('//label[@class="xform_new_address"]/text()')
            #info.append(responsibility)
            writer.writerow(info)   #加入信息
            #writer.writerow(responsibility_department)

if __name__ == '__main__':
    next_url = 'http://eip.megmeet.com:8008/km/review/km_review_main/kmReviewMain.do?method=view&fdId={}'
    login()
    maxpage=input('请输入最大页码:')
    for i in range(1,int(maxpage)+1):
        geterrInfo(i)