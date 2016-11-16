import psycopg2
import pandas as pd
import csv

from sqlalchemy import create_engine
#engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/postgres')
engine = create_engine('postgresql://postgres:rowaway001@localhost:5432/project')
connection = engine.connect()
trans = connection.begin()

sql_text = "select * from genre_info_temp"

col_names = ['movieid','genre']
userdata = pd.read_sql(sql_text,engine,  columns=col_names)

print userdata.head(2)
print userdata.shape
print len(userdata.index)

numpy.zeros((2, len(userdata.index)))
numdata = userdata.as_matrix(columns=None)
with open('C:\\Users\\user\\project\\data\\genre_info.csv', 'wb') as csvfile:
    for i in range(0,len(userdata.index) - 1 ):
        genstring = numdata[i, 1]
        movieidstring = numdata[i, 0]
        splitstring = genstring.split('|')
        for j in range(0,len(splitstring)):
            fieldnames = ['first_name', 'last_name']
            genre_string = str(splitstring[j])
            genrewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
            genrewriter.writerow({'first_name': movieidstring, 'last_name': str(splitstring[j])})
            #inslist.append(splitstring[i])

url = "C:\\Users\\user\\project\\data\\genre_info.csv"
print url

col_names = ['movieid', 'genre']
genreinfo = pd.read_csv(url, header=None, names=col_names, index_col=False)
print genreinfo.head(2)

genreinfo.to_sql('genre_info',engine, chunksize = 100000, if_exists='append', index = False)
