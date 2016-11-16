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

sql_text = "SELECT userid, age_range_desc, gender, occupation_desc \
            FROM \
            user_info users,\
            age_range_param agerange,\
            occupation_param occs\
            where \
            users.age_range_id = agerange.age_range_id and \
            users.occupation_id = occs.occupation_id \
            order by age_range_desc "

col_names = ['userid', 'age_range_desc', 'gender', 'occupation_desc']
userdata = pd.read_sql(sql_text,engine,  columns=col_names)
plots = userdata.occupation_desc.value_counts().plot(kind='barh', fontsize=6, colormap=cmap_bold)

fig = plots.get_figure()
fig.savefig('C:\\Users\\user\\project\\reports\\occupation_demog.jpg')
