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
driver.set_window_size(1400, 700)
url = 'http://192.168.151.140:8075/WebReport/ReportServer?reportlet=ikahe_kanban%2F%5B7ef4%5D%5B4fee%5D%5B62a5%5D%5B8868%5D.cpt'
res = driver.get(url)
print(res)
time.sleep(10)
driver.save_screenshot(r"D:\桌面\repair.png")
print("ok!\n")