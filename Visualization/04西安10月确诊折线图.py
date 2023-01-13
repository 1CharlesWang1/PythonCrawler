import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts


f_China=open("E:\wcl\PythonCrawler\data\crawl_recent_data_of_China.json","r",encoding="UTF-8")
China_data=f_China.read()

#China_data是列表
China_data=json.loads(China_data)

x_data=[]
y_data=[]

#通过循环将日期与确诊人数取出
# i是字典
for all_statistics in China_data:
    print(all_statistics)
    # if(all_statistics['provinceName'])=='陕西省' and all_statistics['dateId']>=20221001:
    #     print(all_statistics)

        # all_statistics['dateId']=str(all_statistics['dateId'])
        # all_statistics['dateId'] = all_statistics['dateId'][0:4] +'.' +\
        #                            all_statistics['dateId'][4:6] + '.' +\
        #                            all_statistics['dateId'][6:8]
        # x_data.append(all_statistics['dateId'])
        # y_data.append(all_statistics['confirmedCount'])

#x,y_data  为列表格式
#y_data需要是字符串
# line=Line()
# line.add_xaxis(x_data)
# line.add_yaxis("西安10月确诊折线图",y_data)
#
#
# line.set_global_opts(
#     title_opts=TitleOpts(title="西安10月确诊折线图",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True,pos_bottom="20%"),
# )
#
# line.render('E:\wcl\PythonCrawler\data\\Shaanxi_Recent_Line_Chart.html')
# f_China.close()