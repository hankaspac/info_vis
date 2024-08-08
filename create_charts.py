import altair as alt
import pandas as pd
import vegafusion as vf
import json
import numpy as np

vf.enable(row_limit=1000000)

alt.renderers.enable('html')

alt.data_transformers.disable_max_rows()
# alt.data_transformers.enable('data_server')

alt.data_transformers.enable('json')

with open('graph_nodes.json') as file:
    books = json.loads(file.read())

my_chart = pd.json_normalize(books)

print(len(my_chart))

my_chart = my_chart[0:10000]

print(len(my_chart))


# TODO nr. of similar books
# TODO look at num_pages - values seem weird
# TODO interval selection in the first graph acts weirdly
# TODO display text filds/windows with descriptions - detail on demand
# TODO add something with displaying books with 1-3 keywords


# interactions:
click = alt.selection_point(encodings=['color'])
click_detail = alt.selection_point() # creates error
interval = alt.selection_interval()
interval_2 = alt.selection_interval()


base = alt.Chart(my_chart).mark_circle(size=100).encode(
    x='average_rating:Q',
    y='publication_year:O',
    color=alt.condition(interval, 'language_code', alt.value('lightgray')),
    size='num_pages:O',
    tooltip='title_without_series:N'
).transform_filter(
    alt.FieldRangePredicate(field='publication_year', range=[1900, 2024])
).transform_filter(
    alt.FieldRangePredicate(field='average_rating', range=[0, 5])
).transform_filter(
    click
).add_params(
    interval    
).properties(
    width=600
).interactive()

base_without_year = alt.Chart(my_chart).mark_circle().encode(
    x='average_rating:Q',
    y='count(similar_books)', #this does not work - it shows some kind of counting but wrongly
    color='language_code',
    size='num_pages:O',
    tooltip='title_without_series'
).transform_filter(
    'datum.publication_year > 2024' and 'datum.publication_year < 1900' or 'datum.publication_year == null' 
).transform_filter(
    alt.FieldRangePredicate(field='average_rating', range=[0, 5])
).transform_filter(
    click
).add_params(
    interval_2   
).properties(
    width=600
).interactive()

chart_with_interval = alt.Chart(my_chart).mark_circle().encode(
    x='average_rating:Q',
    y='publication_year:O',
    size='num_pages:O',
    tooltip='title_without_series:N'
).transform_filter(
    interval_2
).interactive()

sel_values = my_chart['description']
sel_titles = my_chart['title_without_series']

selection_chart = alt.Chart({'values':[{}]}).mark_text( # displays all the descriptions but selection does not work
    align="left", baseline="top"
).encode(
    x=alt.value(5),  # pixels from left
    y=alt.value(5),  # pixels from top
    text=alt.value([f"r: {sel_values}, {sel_titles}"])
).transform_filter(
    interval_2    
)


chart_with_langs = alt.Chart(my_chart).mark_bar().encode(
    x='count()',
    y='language_code',
    # y='average_rating:Q',
    color=alt.condition(click, 'language_code', alt.value('lightgray'))
    # color=alt.condition(click, 'average_rating:Q', alt.value('lightgray'))
).add_params(
    click
).properties(
    width=900,
).interactive()


main_chart = (base | (base_without_year & chart_with_interval & selection_chart)) & chart_with_langs

main_chart.properties(
    width=700,
    height=800
).interactive()

main_chart.save("out_chart.html")
print("weeep")