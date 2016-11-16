import psycopg2
import pandas as pd

from sqlalchemy import create_engine
#engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/postgres')
engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/project')

url = "C:\\Users\\user\\project\\data\\ratings.dat"
print url

col_names = ['userid','movieid','rating','timestamp']
ratingdata = pd.read_csv(url, header=None, names=col_names, index_col=False)

ratingdata.to_sql('ratings',engine, chunksize = 100000, if_exists='append', index = False)
