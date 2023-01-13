from pyecharts.charts import Map
from pyecharts.options import *

map=Map()

data=[
    ("北京",99),
    ("上海",199),
    ("陕西省",9),
    ("湖南",399),
    ("广东",499),
]

map.add("测试地图",data,"china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#f4afb7"},
            {"min":10,"max":99,"label":"10-99","color":"#FF0000"},
            {"min":100,"max":999,"label":"100-999","color":"#8B1A1A"}
        ]
    )
)

map.render()