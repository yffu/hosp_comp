'''
Created on Dec 26, 2013

@author: Yuan-Fang
'''

# import sqlite3 as sqlite
import pymysql
from pymysql import DataError
'''
with sqlite.connect(r"hospitalcompare.db") as lcon:
    lcur=lcon.cursor()
    lcur.execute("select * from hacm")
    for q in lcur.fetchall():
        print q
   '''     
hand1=open('test_error_log.txt', 'wb')
        
with pymysql.connect(db='hc', user='yffu', passwd='1989Oct.2319', host='localhost') as con:
    tmp='insert into HACM values ( 421301, "ABBEVILLE AREA MEDICAL CENTER", "420 THOMSON CIRCLE", "", "", "ABBEVILLE", "SC", 29620, "ABBEVILLE", 8643345665011, "Air bubble in the bloodstream", -1)'
    try:
        con.execute(tmp)
    except DataError as e:
        print e
        hand1.write(e[1]+'\n')
        hand1.write(tmp +'\n')

hand1.close()
