
import altair as alt
import pandas as pd
import json
import numpy as np
import vegafusion as vf
import networkx as nx
import nx_altair as nxa

alt.data_transformers.disable_max_rows()
vf.enable(row_limit=1000000)

f = open('merged_nodes_links.json', 'r')
my_chart2 = json.load(f)
print(type(my_chart2))

G = nx.readwrite.json_graph.node_link_graph(my_chart2, directed=True, multigraph=False)

nxa.draw_networkx(G, node_tooltip=['title_without_series'])