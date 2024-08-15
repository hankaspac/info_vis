import altair as alt
import pandas as pd
import vegafusion as vf
import json
import numpy as np

vf.enable(row_limit=100000000)

alt.renderers.enable('html')

alt.data_transformers.disable_max_rows()
# alt.data_transformers.enable('data_server')

alt.data_transformers.enable('json')

with open('graph_nodes.json') as file:
    books = json.loads(file.read())

my_chart = pd.json_normalize(books)

print(len(my_chart))

my_chart = my_chart[0:1000]

print(len(my_chart))

keywords_description = ["steamy", "vampire"]

def books_with_keywords(words):
    count = 0
    text_file = []
    for i in range(len(my_chart['description'])):
        if words[0] in my_chart['description'][i] and words[1] in my_chart['description'][i]:
            count += 1
            if my_chart['title_without_series'][i] == '':
                text_file.append("The book does not have a title.")
            else:
                text_file.append(my_chart['title_without_series'][i])
                text_file.append("\n")
            text_file.append(my_chart['description'][i])
            text_file.append("\n \n \n")
            
        else:
            continue
    print(count)
    return text_file

text_file = books_with_keywords(keywords_description)
    
with open("file_words.txt", "w") as output:
     output.writelines(text_file)    
#books_with_keywords(keywords_description)

brush = alt.selection_interval()
brush_2 = alt.selection_point()

base = alt.Chart(my_chart).mark_circle(size=100).encode(
    alt.X('average_rating'),
    alt.Y('publication_year:O'),
    # alt.Y(aggregate='count', type='ordinal')
    alt.Color('text_reviews_count:O'),
    alt.Size('count()'),
    # tooltip='title_without_series:N'
).transform_filter(
    alt.FieldRangePredicate(field='publication_year', range=[1900, 2024])
).add_params(
    brush
).properties(
    width=1300,
    height=600
).interactive()

brushed_chart = alt.Chart(my_chart).mark_square().encode(
    alt.X('average_rating'),
    alt.Y('publication_year:O'),
    # alt.Y(aggregate='count', type='ordinal')
    # alt.Color('text_reviews_count:O').bin(),
    tooltip='title_without_series:N'
).transform_filter(
    alt.FieldRangePredicate(field='publication_year', range=[1900, 2024])
).transform_filter(
    brush
).add_params(
    brush_2
).interactive()

print(type(brushed_chart))

# Base chart for data tables
my_text = alt.Chart(my_chart).mark_text(align='left',baseline='middle', color='magenta').encode(
    y=alt.Y('row_number:O', axis=None),
).transform_window(
    row_number='row_number()'
).transform_filter(
    brush_2
).transform_window(
    rank='rank(row_number)'
).transform_filter(
    alt.datum.rank<20
)

# print(type(my_text))

# Data Tables
my_title = my_text.encode(text='title_without_series:N').properties(width=300)
my_description = my_text.encode(text='description:N').properties(width=700)
text = alt.hconcat(my_title, my_description) # Combine data tables


# Build chart
text_chart = alt.vconcat(
    brushed_chart,
    text
)


main_chart = base & text_chart

# main_chart.properties(
#     width=1000,
#     height=1200
# ).interactive()

main_chart.save("out_chart.html")
print("weeep")