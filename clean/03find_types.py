'''
Created on Dec 24, 2013

@author: Yuan-Fang
'''

import os, re, csv, pymysql
import sqlite3 as sqlite
from tools import type_convert, qstr1
from sqlite3 import OperationalError

home_dir="./hc_short"

files= os.walk(home_dir).next()[2]
match_csv=re.compile('(.*)\.csv')

with sqlite.connect(r"hospitalcompare.db") as lcon:
    con = pymysql.connect(db='hc', user='yffu', passwd='1989Oct.2319', host='localhost')
    cur=con.cursor() 
    lcur=lcon.cursor()
    for f in files:
        m=match_csv.search(f)
        if m:
            name=m.group(1)
            cur.execute("select * from name_map where abbr='%s'" % name)
            q= cur.fetchall()
            if q:
                print "opening this file:" , q[0][1]
            with open(home_dir+'/'+f) as handle:
                read=csv.reader(handle, delimiter=',')
                count=0
#                 the first row contains the columns of the table
                ttls=read.next()
                ttls=[re.sub('\W', '', t) for t in ttls]
#                 print "the titles are", ttls
#                 the first set of values, used to determine the types of the variables
                values=read.next()
                values=[re.sub('[$%]', '', v) for v in values]
                values=[type_convert(v) for v in values]
#                     print values
                col_val=[]
#                     create a list of tuples with the column title and the value types
                for i in range(len(values)):
#                         if len(ttls[i])>30:
#                             print "long title: ", ttls[i]
                    col_val.append((ttls[i], values[i][1]))
                qstrings=qstr1(name,col_val)
                try:
                    print "the table creation string: ", qstrings[0]
                    lcur.execute(qstrings[0])
                    raise 
                except OperationalError as e:
                    print "operational error from sqlite",  e
                istr=qstrings[1]
                print "the table insertion string: "
                qstrings[1]=qstrings[1] % tuple(v[0] for v in values)
                print qstrings[1]
#                 lcur.execute('commit')
                lcur.execute(qstrings[1])
#                     print col_val
#                     we still need to make the column names amenable to the sqlite format
                count+=1
                for r in read:
#                     if count >100:
#                         break
#                     else:
                    tmp=istr % tuple(v for v in r)
                    print tmp
                    lcur.execute(tmp)
#                         count +=1
                        
    con.close()
    
    '''
    successfully inserted values of tables into sqlite database;
    now will attempt to insert the values for mysql tables
    '''
