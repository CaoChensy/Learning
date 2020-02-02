# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 10:52
# @Author  : Chensy Cao
# @Email   : chensy.cao@zjtlcb.com
# @FileName: graph_charts.py
# @Software: PyCharm

import os
import json
from pyecharts.charts import Graph
from pyecharts import options as opts

def graph_les_miserables():
    with open(
        os.path.join("dataset", "les-miserables.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)
        nodes = j["nodes"]
        links = j["links"]
        categories = j["categories"]

    c = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=nodes,
            links=links,
            categories=categories,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_left="2%", pos_top="20%"
            ),
        )
    )
    return c

graph_les_miserables().render('./res/graph_chart.html')
