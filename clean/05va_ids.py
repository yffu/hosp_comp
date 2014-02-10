'''
Created on Dec 28, 2013

@author: Yuan-Fang
'''

import re

with open('mysql_ins_log1.txt', 'rb') as hand:
    for row in hand:
        name=re.search('values \(.*?, "(.*?)",' ,row)
        if name:
            print row
            name=name.group(1)
            print name
            
            '''
            as it turns out, the va hospitals did not make it into the hospital general information table either, 
            so 128 entries for the va hospitals are missing from both the hospital general information and the hospital acquired
            infections table. We will ignore these as it will require both changes to the table definition and for us to reinsert 
            all the information again.
            '''