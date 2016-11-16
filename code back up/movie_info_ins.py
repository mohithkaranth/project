import psycopg2
import pandas as pd

from sqlalchemy import create_engine
#engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/postgres')
engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/project')

url = "C:\\Users\\user\\project\\data\\movies.csv"
print url

col_names = ['movieid','title', 'genre']
moviedata = pd.read_csv(url, header=None, names=col_names, index_col=False)
print moviedata.head(2)

movieinfo = moviedata.iloc[:, 0:2]
#movieinfo_py = np.array(movieinfo).reshape(1,-1)

print movieinfo.head(2)
movieinfo.to_sql('movie_info',engine, chunksize = 100000, if_exists='append', index = False)
