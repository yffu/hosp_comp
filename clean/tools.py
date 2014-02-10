'''
Created on Dec 24, 2013

@author: Yuan-Fang
'''
import math


def avg_len(lencnts, ttls):
    avg_lens=dict()
    for i in range(len(ttls)):
        s=sum(lencnts[i])
        c=len(lencnts[i])
        avg_lens[ttls[i]]=s/c
    return avg_lens

def sd_len(lencnts, ttls):
    sd_lens=dict()
    avg_lens=avg_len(lencnts, ttls)
    for i in range(len(ttls)):
        d=[v-avg_lens[ttls[i]] for v in lencnts[i]]
        ssd=sum([math.pow(v,2) for v in d])
        msd=ssd/(len(lencnts[i]))
        sd_lens[ttls[i]]=math.sqrt(msd)
    return sd_lens

# the inserted value is quoted when it is varchar type, no quotations when the type is int or float

def qstr2(name, ttls, types, mean, sds):
    cstr='create table %s (' % name
    istr='insert into %s values (' % name
    for t in ttls:
        cstr+= ' ' + t+' '+types[t]+'(' +(str(int(mean[t]+2*sds[t])) if types[t] in ('numeric', 'float') else str(mean[t]*4)) + '),' 
        istr+=(' %s,' if types[t] in ('float', 'numeric') else ' "%s",')
    cstr=cstr[:-1]+')'
    istr=istr[:-1]+')'
    return [cstr, istr]

# takes name of the table, and a list of the column name and value types, and returns a create table string and a insert sting that can be resued

def qstr1(name, cols):
    cstr='create table %s (' % name
    istr='insert into %s values (' % name
    for c in cols:
        cstr+= ' ' + c[0]+' '+c[1] + ','
        istr+= ' "%s",'
    cstr=cstr[:-1]+')'
    istr=istr[:-1]+')'
    return [cstr, istr]

def qstr(tbl, cols):
    create='create table %s (' % tbl
    insert='insert into %s values (' % tbl
    for c in cols:
        create += ' %s varchar(70),' % c
        insert += " '%s',"
    create=create[:-1]+')'
    insert=insert[:-1]+')'
    return [create, insert]

def build_abbr(name):
    abbr=''
    for n in name.split('_'):
        try:
            abbr+=n[0]
        except:
            continue
    return abbr

def type_convert(val):
    tmp=val
    val_type=''
    try:
        tmp=int(val)
        val_type='integer'
        return [tmp, val_type]
    except:
        None
#         print 'not an integer: ', tmp
    try:
        tmp=float(val)
        val_type='real'
        return [tmp, val_type] 
    except:
        None
#         print 'not a floating point: ', tmp
    val_type='text'
    return [tmp, val_type]

# for use with mysql conventions

def type_convert2(val):
    tmp=val
    val_type=''
    try:
        tmp=int(val)
        val_type='numeric'
        return val_type
    except:
        None
#         print 'not an integer: ', tmp
    try:
        tmp=float(val)
        val_type='float'
        return val_type
    except:
        None
#         print 'not a floating point: ', tmp
    val_type='varchar'
    return val_type

def type_convert3(val, type):
    try:
        if type=='float':
            return float(val)
        elif type=='numeric':
            return int(val)
        elif type=='varchar':
            return val
        else:
            None
    except TypeError as e:
        print e
        return None
    except ValueError as e:
        print e
        print "failed to convert val", val, "to type ", type
        if type in ('float', 'int'):
            return -1