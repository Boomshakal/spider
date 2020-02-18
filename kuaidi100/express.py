import json
import requests

num = input('请输入要查单号:')
company_url = 'https://m.kuaidi100.com/apicenter/kdquerytools.do?method=autoComNum&text={}'  # 这里是用来找特定文件提取特定的单号对应的公司信息
company = requests.get(company_url.format(num))
print(company.text)
if company.status_code != 200:
    print('查询失败！')
    exit()
else:
    jsonobj = json.loads(company.text)  # 原代码中Json格式已经很整齐了，只需要找到需要的信息
    # print(jsonobj)
    for item in jsonobj.get('auto'):
        com = item.get('comCode')
        url = 'https://www.kuaidi100.com/query?type={}&postid={}'.format(com, num)  # 观察到了快递信息所对应链接格式，根据单号和公司构建所需链接
        response = requests.get(url)
        if response.status_code != 200:
            print('查询失败!')
        else:
            mes = json.loads(response.text)
            print(com + mes.get('message'))
            if mes.get('message') == 'ok':
                for data in mes.get('data'):
                    print('%s %s' % (data.get('time'), data.get('context')))  # 输出快递信息
