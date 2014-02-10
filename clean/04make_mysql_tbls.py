'''
Created on Dec 26, 2013

@author: Yuan-Fang
'''
import os, re, pymysql, csv
from tools import avg_len, sd_len, type_convert2, type_convert3, qstr2
from pymysql import InternalError, DataError, InternalError

home_dir="./hc_short"
csv_match=re.compile('^(.*\.csv)$')

files= os.walk(home_dir).next()[2]

hand1=open('mysql_ins_log.txt', 'wb')

with pymysql.connect(db='hc', user='yffu', passwd='1989Oct.2319', host='localhost') as con:
    all_types=dict()
    istrs=dict()
    for f in files:
        f_name=re.search('^(.*)\.csv$', f).group(1)
        with open(home_dir+'/'+f, 'r') as hand:
            read=csv.reader(hand, delimiter=',')
            print "using the file ", f_name
#             get the titles for the files
            ttls=read.next()
            ttls=[re.sub('\W', '', v) for v in ttls]
            print "with the titles ", ttls
#             loop through the first 100 entries, and sum the values
            lengthcnts=[[] for t in ttls]
            cnt=0
            title_length=len(ttls)
            while cnt<100:
                vals=read.next()
                for i in range(title_length):
                    lengthcnts[i].append(len(vals[i]))
                cnt+=1
            avg_lens=avg_len(lengthcnts, ttls)
            sd_lens=sd_len(lengthcnts, ttls)
            print "average length of entries in first 100 ",  avg_lens
            print "standard deviation of entries in first 100 ", sd_lens
#             get the next line and find the types of the values
            vals=[re.sub('[$%]', '', v) for v in read.next()]
            type_vals=dict()
            for i in range(len(vals)):
                type_vals[ttls[i]]=type_convert2(vals[i])
            print "the types of values for mysql ", type_vals
            qstrings=qstr2(f_name, ttls, type_vals, avg_lens, sd_lens)
            print "the creation string: ", qstrings[0]
            istr=qstrings[1]
            print "the insertion string: ", istr
            istrs[f_name]=istr
            all_types[f_name]=type_vals
#             use the creatin string to create the tables, create only once
            try:
                con.execute(qstrings[0])
            except InternalError as e:
                print "the mysql execution failed, message: ", e
#                 loop around the files around to do the insertions
    files= os.walk(home_dir).next()[2]
    print istrs
    for f in files:
        f_name=re.search('^(.*)\.csv$', f).group(1)
        with open(home_dir+'/'+f, 'r') as hand:
            read=csv.reader(hand, delimiter=',')
            print "using the file ", f_name
            istr=istrs[f_name]
            types=all_types[f_name]
            print "insertion string: ", istr
            ttls=read.next()
            ttls=[re.sub('\W', '', v) for v in ttls]
            cnt=0
            for r in read:
#                 if cnt>3:
#                     break
#                 else:
                tmpstr=istr % tuple(type_convert3(re.sub('[%$]', '', r[i]), types[ttls[i]]) for i in range(len(r)))
                print tmpstr
                try:
                    con.execute(tmpstr)
                except DataError as e:
                    print e
                    hand1.write(e[1]+'\n')
                    hand1.write(tmpstr+'\n')
                except InternalError as e:
                    print e
                    hand1.write(e[1]+'\n')
                    hand1.write(tmpstr+'\n')
hand1.close()                  
#                     cnt+=1
