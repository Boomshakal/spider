# import requests
#
# url = 'http://192.168.151.140:8075/WebReport/ReportServer?reportlet=ikahe_kanban%2Fxqhz.cpt'
#
# res = requests.get(url)
# print(res.text)

from selenium import webdriver
import time

print("start....\n")
driver = webdriver.PhantomJS()
url = 'http://192.168.151.140:8075/WebReport/ReportServer?reportlet=ikahe_kanban%2Fxqhz.cpt'
res = driver.get(url)
print(res)
# driver.save_screenshot("kanban.jpeg")
print("ok!\n")