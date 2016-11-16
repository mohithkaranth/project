import psycopg2
import pandas as pd
import csv

import matplotlib.pyplot as plt

# increase default figure and font sizes for easier viewing
plt.rcParams['figure.figsize'] = (6, 4)
plt.rcParams['font.size'] = 14

# create a custom colormap
from matplotlib.colors import ListedColormap
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


from sqlalchemy import create_engine
#engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/postgres')
engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/project')
connection = engine.connect()
trans = connection.begin()

sql_text = "SELECT  movieid, genre FROM genre_info gen"

col_names = ['movieid', 'genre']
scatdata = pd.read_sql(sql_text,engine,  columns=col_names)
scatdata = scatdata.convert_objects(convert_numeric=True)
plots = scatdata.plot(kind='hist', x= 'genre', y = 'movieid' , fontsize=8, colormap=cmap_bold)

fig = plots.get_figure()
fig.savefig('C:\\Users\\user\\project\\reports\\genre_scatter.jpg')
