# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 22:29:28 2021

@author: manle
"""

import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine

conda install pymysql
import pymysql

MYSQL_HOSTNAME = '52.249.196.193'
MYSQL_USER = 'DBA'
MYSQL_PASSWORD = 'ahi2021'
MYSQL_DATABASE = 'e2e'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

print (engine.table_names())


h1n1 = pd.read_csv(r'C:\Users\manle\Downloads\H1N1FluVaccines.csv')
h1n1.to_sql('h1n1', con=engine, if_exists='append')

