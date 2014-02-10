'''
Created on Dec 27, 2013

@author: Yuan-Fang
'''
import os, re, pymysql, csv
from tools import avg_len, sd_len, type_convert2, type_convert3, qstr2
from pymysql import InternalError, DataError

# go through the values that did not insert into mysql, find out table names and values

def commarepl(matchobj):
#     print matchobj.group(1)   
#     print matchobj.group(0) 
# group1 contains the number part of the string, while group0 contains teh entire query string
#   replace the comma inside of group1, and replace the new group1 inside of group0
    if ',' in matchobj.group(1): return re.sub(matchobj.group(1),  re.sub(',', '', matchobj.group(1)), matchobj.group(0))
    else: return matchobj.group(0)

tbl_dict=dict()

hand1=open('mysql_ins_log1.txt', 'w')

with open('mysql_ins_log.txt', 'r') as hand:
    with pymysql.connect(db='hc', user='yffu', passwd='1989Oct.2319', host='localhost') as con:
    #     cnt=0
        for row in hand:
            ins_match=re.match('^insert into (.*) values\((.*)\)$', row)
    #         if cnt>100:
    #             break
            if not ins_match:
                ins_str=hand.next()
                val_type=re.search("'(.*?)'", row)
                if val_type:
                    val_type=val_type.group(1)
    #                 print val_type
                    ins_match=re.match('^insert into (.*) values(.*)$', ins_str)
                    if ins_match:
                        tbl_name=ins_match.group(1)
                        tbl_vals=ins_match.group(2)
    #                     print "find in table ", tbl_name, "the values", tbl_vals  
                        tbl_dict[tbl_name]=tbl_dict.get(tbl_name, dict())
                        tbl_dict[tbl_name][val_type]=tbl_dict[tbl_name].get(val_type, 0)+1
#                         for the hai footnotes that were too long
                        if val_type=="Footnote" and tbl_name=="HAI":
                            print tbl_vals
                            footnote=re.search('.*, "(.*?)",.*?\)$', tbl_vals)
                            try:
                                strg='insert into table HAI values '+tbl_vals
                                con.execute(ins_str)
                            except:
                                print "failed to insert: ", ins_str
                                hand1.write(ins_str+'\n')
                            if footnote:
                                footnote=footnote.group(1)
                                print footnote
                                print len(footnote)
                        if val_type=='Footnote' and tbl_name=="MSPP":
#                             print tbl_vals
                            try:
                                strg='insert into table MSPP values '+tbl_vals
                                con.execute(ins_str)
                            except:
                                print "failed to insert: ", ins_str
                                hand1.write(ins_str+'\n')
                            footnote=re.search('.*, "(.*?)"\)$', tbl_vals)
                            if footnote:
                                footnote=footnote.group(1)
#                                 found the footnote length for mspp, changed column type in mysql
#                                 print tbl_name
#                                 print footnote
#                                 print len(footnote)
#                             con.execute('try it again')
                        elif val_type=='NumberOfCases':
                            t_match=re.search('.*"(.*?)",.*\)$', tbl_vals)
                            if t_match:
                                t_match=t_match.group(1)
                                t_sub=re.sub('.*"(.*?)",.*\)$', commarepl, tbl_vals)
                                print t_sub                                
                                try:
                                    None
#                                     strg='insert into HMVM values '+t_sub
#                                     con.execute(strg)
                                except:
                                    None
                                    print "failed to insert: ", strg
                                    hand1.write(tbl_vals+'the substituted string'+strg+'\n')
                        elif val_type=='None':
                            hand1.write(ins_str)
                            
#                             print tbl_vals
                        else:
                            None
            else:
                None
    #         cnt+=1

hand1.close()
# print a summary of the cases that were missed
print tbl_dict


# here's a summary of the cases that were missed
'''
the footnotes in MSPP and HAI are too long, 

some providerid in the HGI table have alha characters, for the VA hospitals. need to reinsert the values

in HMVM, the number of cases has the commas that separate the thousands, and this errors out.

need to see if the column definitions can be changed in mysql without changing existing values 

HMVM values added, as well as the footnotes sections, the VA hospital ids are lost and have to be found some other way

'''