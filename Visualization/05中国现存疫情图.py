import json
from pyecharts.charts import Map
from pyecharts.options import *

#打开文件
f_China=open("E:\wcl\PythonCrawler\data\crawl_last_day_data_of_China.json",encoding="UTF-8")
data=f_China.read()
#str格式转换为python的list
China_total_list=json.loads(data)

China_current_list=[]

# print(China_list)
#循环获取列表数据
for provice_data in China_total_list:
    provice_name=provice_data['provinceShortName']
    provice_current_count=provice_data['currentConfirmedCount']
    # print(provice_name,':',provice_current_count)
    China_current_list.append((provice_name,provice_current_count))

print(China_current_list)

#建立图表
map=Map()
map.add("各省现存确诊",China_current_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-9","color":"#f4afb7"},
            {"min":100,"max":499,"label":"10-99","color":"red"},
            {"min":499,"max":999,"label":"10-99","color":"#CD2626"},
            {"min":1000,"max":999999999,"label":"100-999","color":"#8B1A1A"}
        ]
    )
)

map.render("E:\wcl\PythonCrawler\data\China_last_day_chart.html")
f_China.close()







