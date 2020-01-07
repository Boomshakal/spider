# -*- coding: utf-8 -*-
import requests
import html
import re

USERNAME = 'admin'
PASSWORD = 'megmeet@p!@#$%8awdsz'
URL = 'http://122.226.143.230:8028/MesWebService.asmx'


class Mes(object):

    def SaveCheckData(self, xmlstr):
        headers = {
            'Host': '122.226.143.230:8028',
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': "http://tempuri.org/SaveCheckData",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        body = """<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                      <soap:Header>
                        <MySoapHeader xmlns="http://tempuri.org/">
                          <UserName>{UserName}</UserName>
                          <PassWord>{PassWord}</PassWord>
                        </MySoapHeader>
                      </soap:Header>
                      <soap:Body>
                        <SaveCheckData xmlns="http://tempuri.org/">
                          <xmlstr>{xmlstr}</xmlstr>
                        </SaveCheckData>
                      </soap:Body>
                    </soap:Envelope>
                """
        body = body.format(UserName=USERNAME, PassWord=PASSWORD, xmlstr=html.escape(xmlstr))
        res = requests.post(url=URL, data=body.encode(), headers=headers)

        str = html.unescape(res.text)
        result = re.findall('<SaveCheckDataResult>(.*?)</SaveCheckDataResult>', str, re.S | re.M)
        return result[0]

    def CheckBarcode(self, xmlstr):
        headers = {
            'Host': '122.226.143.230:8028',
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': "http://tempuri.org/CheckBarcode",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        body = """<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                      <soap:Header>
                        <MySoapHeader xmlns="http://tempuri.org/">
                          <UserName>{UserName}</UserName>
                          <PassWord>{PassWord}</PassWord>
                        </MySoapHeader>
                      </soap:Header>
                      <soap:Body>
                        <CheckBarcode xmlns="http://tempuri.org/">
                          <xmlstr>{xmlstr}</xmlstr>
                        </CheckBarcode>
                      </soap:Body>
                    </soap:Envelope>
                """

        body = body.format(UserName=USERNAME, PassWord=PASSWORD, xmlstr=html.escape(xmlstr))
        res = requests.post(url=URL, data=body.encode(), headers=headers)

        str = html.unescape(res.text)
        result = re.findall('<CheckBarcodeResult>(.*?)</CheckBarcodeResult>', str, re.S | re.M)
        return result[0]

    def CheckInitPar(self, xmlstr):
        headers = {
            'Host': '122.226.143.230:8028',
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': "http://tempuri.org/CheckInitPar",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        body = """<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                      <soap:Header>
                        <MySoapHeader xmlns="http://tempuri.org/">
                          <UserName>{UserName}</UserName>
                          <PassWord>{PassWord}</PassWord>
                        </MySoapHeader>
                      </soap:Header>
                      <soap:Body>
                        <CheckInitPar xmlns="http://tempuri.org/">
                          <xmlstr>{xmlstr}</xmlstr>
                        </CheckInitPar>
                      </soap:Body>
                    </soap:Envelope>
                """
        body = body.format(UserName=USERNAME, PassWord=PASSWORD, xmlstr=html.escape(xmlstr))
        res = requests.post(url=URL, data=body.encode(), headers=headers)

        str = html.unescape(res.text)
        result = re.findall('<CheckInitParResult>(.*?)</CheckInitParResult>', str, re.S | re.M)
        return result[0]

    def get(self):
        res = requests.get(url=URL)

        return res.text


if __name__ == '__main__':
    '''
    Sequence = {
    'M081':'接地测试',
    'M082' : '性能测试',    
    'M083':'安规测试',        
    }
    
    后台数据库存储过程：p_fm_work_create_for_test
    '''
    xmlstr = """
    <Parameters>
        <appSettings>
            <head Result="PASS" BarCode="YQX320000000010" TaskOrder="MO18020037-02"  WorkLine ="Line2（包装）"  WorkStation="pk"   WorkShift ="夜班"  Sequence="M083"  WorkDevice =""  Worker ="m00000873"  WorkLeader ="M00000760"  Department ="IKAHE"  UserCode="M00000873"  />
        </appSettings>
        <items>
            <item step="0" item="安规测试" title="安规测试" max="1111" min="123321" value="123" result="PASS" unit="mA" time="2019-12-17"/>
        </items>
    </Parameters>
    """

    mes = Mes()
    check_init_result = mes.CheckInitPar(xmlstr)

    if check_init_result == 'OK':
        check_barcode_result = mes.CheckBarcode(xmlstr)
        if check_barcode_result == 'OK':
            save_result = mes.SaveCheckData(xmlstr)
            print('save_result :', save_result)
        else:
            print('check_result :', check_barcode_result)
    else:
        print('check_init_result :', check_init_result)
