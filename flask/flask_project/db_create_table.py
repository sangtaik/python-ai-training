#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create table
from select import select
import pymysql

db = pymysql.connect(host='localhost', user='root', db='python',
                     password='password', charset='utf8')
curs = db.cursor()

sql = '''create table sample (
    column01 varchar(50),
    column02 varchar(50),
    column03 varchar(50))
'''

curs.execute(sql)


sql = "select * from sample"
curs.execute(sql)

sql = "insert into sample (column01, column02,column03)values ('aa', 'bb', 'cc')"
curs.execute(sql)
db.commit()

sql = "select * from sample"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

for row in rows:
    print(row)

db.commit()
db.close()





