from tqdm import tqdm
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd
import numpy as np

position = [ "北京", "天津", "上海", "重庆", "河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "香港", "澳门"]
name,level,hot,address,num,price=[],[],[],[],[],[]

def get_one_page(key,page):
    try:
    #打开浏览器窗口
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_argument( '--headless')
        driver = webdriver.Chrome(chrome_options=option_chrome)
        time.sleep(1)
        url = "http://piao.qunar.com/ticket/list.htm?keyword="+str(key)+ "&region=&from=mpl_search_suggest&page="+str(page)
        driver.get(url)
        infor = driver.find_elements_by_class_name( "sight_item")
        for i in range(len(infor)):
        #获取景点名字
            name.append(infor[i].find_element_by_class_name( "name").text)
        #获取景点评级
            try:
                level.append(infor[i].find_element_by_class_name( "level").text)
            except:
                level.append( "")
            #获取景点热度
            hot.append(infor[i].find_element_by_class_name( "product_star_level").text[ 3:])
            #获取景点地址
            address.append(infor[i].find_element_by_class_name( "area").text)
            #获取景点销量
            try:
                num.append(infor[i].find_element_by_class_name( "hot_num").text)
            except:
                num.append( 0)
            price.append(infor[i].find_element_by_class_name("sight_item_price").text)
        driver.quit()
        return
    except TimeoutException or WebDriverException:
        return get_one_page()

for key in tqdm(position):
    print( "正在爬取{}".format(key))
    #取前10页
    for page in range(1,11):
        print( "正在爬取第{}页".format(page))
        get_one_page(key,page)
sight = { 'name': name, 'level': level, 'hot': hot, 'address': address, 'num':num, 'price':price}
sight = pd.DataFrame(sight, columns=[ 'name', 'level', 'hot', 'address', 'num', 'price'])
sight.to_csv( "sight1.csv",encoding= "utf_8_sig")
