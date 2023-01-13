import json
from pyecharts.charts import Map
from pyecharts.options import *

#打开文件
f_China=open("E:\wcl\PythonCrawler\data\crawl_last_day_data_of_China.json",encoding="UTF-8")
data=f_China.read()
#str格式转换为python的list
China_total_list=json.loads(data)

Shaanxi_total_dict=China_total_list[9]
Shaanxi_total_list=Shaanxi_total_dict['cities']

Shaanxi_current_list=[]

# 循环获取列表数据
for city_data in Shaanxi_total_list:
    city_name=city_data['cityName']+"市"
    city_current_count=city_data['currentConfirmedCount']
    Shaanxi_current_list.append((city_name,city_current_count))

print(Shaanxi_current_list)

#建立图表
map=Map()
map.add("陕西现存确诊",Shaanxi_current_list,"陕西")
map.set_global_opts(
    title_opts=TitleOpts(title="陕西疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#f4afb7"},
            {"min":10,"max":49,"label":"10-49","color":"red"},
            {"min":50,"max":99,"label":"50-99","color":"#CD2626"},
            {"min":100,"max":9999,"label":"100-9999","color":"#8B1A1A"}
        ]
    )
)

map.render("E:\wcl\PythonCrawler\data\Shaanxi_last_day_chart.html")
f_China.close()







