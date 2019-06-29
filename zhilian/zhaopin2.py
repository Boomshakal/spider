import csv
import json
from urllib import request, parse
from http import cookiejar
from lxml import etree

import requests

url = 'https://apiapp.zhaopin.com/ihrapi/resume/resumelistbykey?access_token=5e730e1b5ccd45f884fc59d3175b2fe1&startNum=20&rowsCount=20&source=1&jobNo=&orderFlag=deal'
headers = {
    'Host': 'apiapp.zhaopin.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'x-zp-device-id=baf4cd2f5f4f91805eefd5af9933d9cf; x-zp-client-id=be2de5ef-563b-4006-acb4-f73ecd427a87; sajssdk_2015_cross_new_user=1; sts_deviceid=16b4eca972d5d6-057f59ed9271b1-e353165-1638720-16b4eca972f516; dywez=95841923.1560395028.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; __utmz=269921210.1560395028.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); urlfrom2=121113803; adfbid2=0; zp-route-meta=uid=132787351,orgid=25272202; login_point=25272202; promoteGray=; NTKF_T2D_CLIENTID=guest8DCEC7C1-BD7E-64E2-4969-4ECB5268176C; diagnosis=0; __utma=269921210.1727489822.1560395028.1560395028.1560412717.2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22132787351%22%2C%22%24device_id%22%3A%2216b4eca95c314c-0f6919a300b3ad-e353165-1638720-16b4eca95c474%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216b4eca95c314c-0f6919a300b3ad-e353165-1638720-16b4eca95c474%22%7D; hideAnnounceNotify=1; dywea=95841923.3887055483229229000.1560395028.1560412717.1560417767.3; dywec=95841923; __utmc=269921210; login-type=b; nTalk_CACHE_DATA={uid:kf_9051_ISME9754_25272202,tid:1560417793115387}; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fpassport.zhaopin.com%2Forg%2Flogin; at=57b2c4b30eff4a50ba689ca0ad113bac; rt=9d41bb1d0a734f40b3a0c836e4285c0b',

}
result = requests.get(url=url, headers=headers)

print(result.text)
