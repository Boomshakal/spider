import requests

url = 'http://58.250.30.13:55599/pedicure/web/equipment/thirdAddEquipment'

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
data = {
    "account": "saiyiPedicures",
    "password": "saiyi_huaan",
    "name": "SmartBidet",
    "code": "SDFE4545445",
    "type": "2",
    "status": "4",
    "address": "",
    "model": "F1R",
    "machineCode": "SDFE4545445987465454",
    "provinceAgent": "",
    "cityAgent": "",
    "hotelAgent": ""
}

result = requests.post(url=url, json=data, headers=headers)
print(result.text)
