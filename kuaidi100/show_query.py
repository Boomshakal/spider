# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
import json

import requests
from ShowapiRequest import ShowapiRequest

num = input('请输入要查单号:')
company_url = 'https://m.kuaidi100.com/apicenter/kdquerytools.do?method=autoComNum&text={}'  # 这里是用来找特定文件提取特定的单号对应的公司信息
company = requests.get(company_url.format(num))
jsonobj = json.loads(company.text)
com = jsonobj.get('auto')[0].get('comCode')

r = ShowapiRequest("http://route.showapi.com/64-19", "147896", "07dc42e232a0417288102898eb8dabd6")
r.addBodyPara("com", com)
r.addBodyPara("nu", num)
r.addBodyPara("senderPhone", "")
r.addBodyPara("receiverPhone", "")
r.addBodyPara("callBackUrl", "")
r.addBodyPara("contentType", "bodyString")
res = r.post()
print(res.text)  # 返回信息
