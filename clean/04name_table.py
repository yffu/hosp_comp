'''
Created on Dec 24, 2013

@author: Yuan-Fang
'''

import csv, pymysql
from tools import qstr

# put the values in the abbreviations table into the name_map table

with pymysql.connect(user='yffu', passwd='1989Oct.2319', host='localhost') as cur:
    cur.execute('create database if not exists hc')
    cur.execute('use hc')
    with open('abbreviations.csv', 'r') as hand:
        read=csv.reader(hand, delimiter='\t')
        ttl=read.next()
        temp=qstr('name_map', ttl)
        cur.execute('drop table if exists name_map')
        create= temp[0]
        insert= temp[1]
        cur.execute(create)
        for line in read:
            if len(line)==3:
                print line
                tmp= insert % tuple(l for l in line)
                print tmp
                cur.execute(tmp) 
#         for r in read:
#             print r