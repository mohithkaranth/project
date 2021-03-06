import psycopg2
import pandas as pd

from sqlalchemy import create_engine
#engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/postgres')
engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/project')

url = "C:\\Users\\user\\project\\data\\users.csv"
print url

col_names = ['userid','gender', 'age_range_id','occupation_id','zip_code']
userdata = pd.read_csv(url, header=None, names=col_names, index_col=False)

userdata.to_sql('user_info',engine, chunksize = 100000, if_exists='append', index = False)
