import pandas as pd

data = pd.read_csv("sight.csv")
data = data.fillna(0)
data = data.drop(columns=['Unnamed: 0'])
#将地址分为省，市，区
data["address"] = data["address"].apply(lambda x: x.replace("[","").replace("]",""))
data["province"] = data["address"].apply(lambda x: x.split("·")[0])
data["city"] = data["address"].apply(lambda x: x.split("·")[1])
data["area"] = data["address"].apply(lambda x: x.split("·")[-1])
#销量最多的前30景点
num_top = data.sort_values(by = 'num',axis = 0,ascending = False).reset_index( drop= True)

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams[ 'font.sans-serif'] = [ 'Microsoft YaHei'] #指定默认字体
plt.rcParams[ 'axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题
sns.set(font= 'SimHei') # 解决Seaborn中文显示问题
sns.set_context( "talk")
fig = plt.figure(figsize=( 15, 10))
sns.barplot(num_top[ "name"][: 30],num_top[ "num"][: 30])
plt.xticks(rotation= 90)
fig.show()

#省份与景区评级

data[ "level_sum"] = 1
var= data.groupby([ 'province', 'level']).level_sum.sum()
var.unstack().plot(kind= 'bar',figsize=( 35, 10), stacked= False, color=[ 'red', 'blue', 'green', 'yellow'])

#根据省、市统计销量和

pro_num = data.groupby([ 'province']).agg( 'sum').reset_index()
city_num = data.groupby([ 'city']).agg( 'sum').reset_index()

#基于数据做热力图
'''
import requests

def transform(geo):

    key= 'bb9a4fae3390081abfcb10bc7ed307a6'
    url= "http://restapi.amap.com/v3/geocode/geo?key="+ str( key) + "&address="+ str(geo)
    print(url)
    response = requests.get( url)

    if response.status_code == 200:

        answer = response.json()

        try:

            loc = answer[ 'geocodes'][ 0][ 'location']
        except:

            loc = 0

    return loc

pro_num[ "lati"] = pro_num[ "province"].apply(lambda x: transform(x))
city_num[ "lati"] = city_num[ "city"].apply(lambda x: transform(x))
'''
pro_num.to_csv( "pro_num.csv", encoding= "utf_8_sig")
city_num.to_csv( "city_num.csv", encoding= "utf_8_sig")

from pyecharts import Map

map= Map( "省份景点销量热力图", title_color= "#fff", title_pos= "center", width= 1200, height= 600, background_color= '#404a59')

map.add( "",pro_num[ "province"], pro_num[ "num"], maptype= "china", visual_range=[ 5000, 80000], is_visualmap= True, visual_text_color= '#000', is_label_show= True)

map.render( path= "pro_num.html")

map= Map( "省份景点热度热力图", title_color= "#fff", title_pos= "center", width= 1200, height= 600, background_color= '#404a59')

map.add( "",pro_num[ "province"], pro_num[ "hot"], maptype= "china", visual_range=[ 25, 80], is_visualmap= True, visual_text_color= '#000', is_label_show= True)

map.render( path= "pro_hot.html")

#人少的5A景点，4A景点，3A景点

top_5A = data[ data[ "level"] == "5A景区"].sort_values( by= 'num',axis = 0,ascending = True).reset_index( drop= True)
top_4A = data[ data[ "level"] == "4A景区"].sort_values( by= 'num',axis = 0,ascending = True).reset_index( drop= True)
top_3A = data[ data[ "level"] == "3A景区"].sort_values( by= 'num',axis = 0,ascending = True).reset_index( drop= True)

fig = plt.figure(figsize=( 15, 15))
plt.pie(top_5A[ "num"][: 15],labels=top_5A[ "name"][: 15],autopct= '%1.2f%%')
plt.title( "人少的5A景区")

plt.show()

fig = plt.figure(figsize=( 15, 15))
ax = sns.barplot(top_4A[ "hot"][: 15],top_4A[ "name"][: 15])
ax.set_title( "人少的4A景区")

fig.show()

fig = plt.figure(figsize=( 15, 10))
ax = sns.barplot(top_3A[ "name"][: 15],top_3A[ "hot"][: 15])
ax.set_title( "人少的3A景区")

plt.xticks(rotation= 90)

fig.show()