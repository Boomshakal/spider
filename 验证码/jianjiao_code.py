import requests
import base64
import json


def check_code():
    f = open('checkCode.jpg', 'rb')
    im_base64 = base64.b64encode(f.read())

    host = 'http://apigateway.jianjiaoshuju.com'
    path = '/api/v_1/yzm.html'

    appcode = '5A6FE1F6621124D8E9C72341AF875876'
    appKey = 'AKID0d22f1d01bb45f97bf0b90abf6003efc'
    appSecret = '5135e7a33b079aecc65babab5d1b9cda'

    bodys = {
        'v_pic': im_base64,
        'v_type': 'ne4',
    }

    url = host + path

    headers = {
        'appcode': appcode,
        'appKey': appKey,
        'appSecret': appSecret,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    response = requests.post(url=url, data=bodys, headers=headers)
    content = json.loads(response.text)
    if content:
        return content['v_code']


if __name__ == '__main__':
    code = check_code()
    print(code)