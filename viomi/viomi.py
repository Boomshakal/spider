import requests
import json


class Viomi():

    def __init__(self):
        uuid = 0

    def getuuid(self):
        url = 'https://factory-qa-service.viomi.com.cn/qalogin'

        data = {
            'account': 'yihescan',
            'pwd': 'yihe2019'
        }

        result = requests.post(url=url, data=data)
        uuid = json.loads(result.text)['data']['uuid']
        return uuid

    def getdata(self,uuid):
        url = 'https://factory-qa-service.viomi.com.cn/api/macsn/manage/getPreData'
        params = {
            'type': '26',
            'factory': 'yihe',
            'order_desc': 'sn_time',
            'sn_time_min': '2019-11-26 00:00:00',
            'sn_time_max': '2019-11-26 23:59:59',
            '_uuid': uuid
        }

        resutl = requests.get(url=url,params=params)
        return resutl.text


if __name__ == '__main__':
    viomi = Viomi()
    print(viomi.getdata(viomi.getuuid()))
    # print(viomi.getuuid())
