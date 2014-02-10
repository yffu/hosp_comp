'''
Created on Dec 24, 2013

@author: Yuan-Fang
'''
import os, re
from tools import build_abbr

home_dir="./hc"
csv_match=re.compile('^(.*\.csv)$')

if not os.path.exists(home_dir):
    print "home_dir not exists"
    os.makedirs(home_dir)

files= os.walk(home_dir).next()[2]

# for moving the files from current to hc directory
'''
for t in files:
    m=csv_match.search(t)
    if m:
        file_name=m.group(0)
        print file_name
        os.rename('./'+ file_name, home_dir+'/'+file_name)
        '''

# removes state and national average files:
        
'''
for f in files:
    m= re.search('State|National', f)
    if m:
        os.remove(home_dir+'/'+f)
        
'''
        
# shorten the filenames for process of care entries

'''
for f in files:
    m=re.search('Hospital_Process_of_Care_Measures_(.*)\.csv$'.lower(), f.lower())
    if m:
        part=m.group(1)
#         print "from:", home_dir+'/'+f  
        print "to:", home_dir+'/'+'POC_'+part+'.csv'
        os.rename(home_dir+'/'+f, home_dir+'/'+'POC'+part+'.csv')
        '''
        
# further abbreviate the process of care filenames
'''
for f in files:
    m=re.search('POC(.*)\.csv$'.lower(), f.lower())
    if m:
        part=m.group(1)
    #             print part, '\t', build_abbr(part)
        o= part
        a= 'POC'+'_'+build_abbr(part)
        print "original title:", o
        print "abbr title:", a
        print home_dir+'/'+f
        print home_dir+'/'+a+'.csv'
        os.rename(home_dir+'/'+f, home_dir+'/'+a+'.csv')
'''
# repeat for the hvbp files
'''
for f in files:
    m=re.search('^(.*)_HVBP_(.*)\.csv$', f)
    if m:
        cat=build_abbr(m.group(1))
        type=build_abbr(m.group(2)).lower()
        a= cat+'_'+type
        print home_dir+'/'+f
        print home_dir+'/'+a+'.csv'
        os.rename(home_dir+'/'+f, home_dir+'/'+a+'.csv')
'''

# rename the files that do not belong in broad categories
'''
for f in files:
    m=re.search('HVBP|POC', f)
    if not m:
        m=re.search('^(.*)\.csv$', f)
        ttl=m.group(1)
        a=build_abbr(ttl).upper()
        ttl= re.sub('_', ' ', ttl ).strip()
        print home_dir+'/'+f
        print home_dir+'/'+a +'.csv'
        os.rename(home_dir+'/'+f, home_dir+'/'+a +'.csv')
        '''