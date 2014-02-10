'''
Created on Dec 24, 2013

@author: Yuan-Fang
'''

import os, re, csv
from tools import build_abbr

home_dir="./hc"
files= os.walk(home_dir).next()[2]

# create abbreviations file, with categories for larger tables such as hospital process of care
# with tables split off for each categories

# write the titles for the file

#     abbrw.writerow(['category','tblname', 'abbr'])


'''

with open('abbreviations.csv', 'w') as abbr:
    abbrw=csv.writer(abbr, delimiter="\t")
    for f in files:
        ttl='Hospital_Process_of_Care_Measures'
        m=re.search('POC(.*)\.csv$'.lower(), f.lower())
        if m:
            part=m.group(1)
#             print part, '\t', build_abbr(part)
            o= part
            a= 'POC'+'_'+build_abbr(part)
            print "original title:", o
            print "abbr title:", a
            abbrw.writerow([ttl, o , a])
'''



# apply the same to hospital value based program

'''
with open('abbreviations.csv', 'a') as abbr:
    abbrw=csv.writer(abbr, delimiter="\t")
    for f in files:
        m=re.search('^(.*)_HVBP_(.*)\.csv$', f)
        if m:
            category= m.group(1)
            type=m.group(2)
            print category
            print type
            a=build_abbr(category)+'_'+ build_abbr(type).lower()
            print a 
            abbrw.writerow([category, type , a])
            '''
            
# do the abbreviations for the rest of the titles
'''
with open('abbreviations.csv', 'a') as abbr:  
    abbrw=csv.writer(abbr, delimiter="\t")       
    for f in files:
        m=re.search('HVBP|POC', f)
        if not m:
            m=re.search('^(.*)\.csv$', f)
            ttl=m.group(1)
            a=build_abbr(ttl).upper()
            ttl= re.sub('_', ' ', ttl ).strip()
            print ttl
            print a
            abbrw.writerow(['None',ttl , a])
            '''