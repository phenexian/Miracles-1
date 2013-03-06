#!/usr/bin/python
# Filename: Numeral reader

s="MMMCCDXIIV"
lst=[]
dictionary=[["M",1000],["D",500],["C",100],["L",50],["X",10],["V",5],["I",1]]

def read(s):
    res=0
    sgn=+1
    a=0
    bsf=0
    for i in range(1,len(s)+1):
        for n in dictionary:
            if n[0]==s[-i]:
                b=n[1]
                
        if sgn==-1 and bsf<b:
            bsf=b
            sgn=+1
        elif bsf<b:
            bsf=b
            
        if b<a:
            sgn=-1
              
        a=b
        res=res+(sgn*b)
    return res

def write(n):
    s=""
    for i in dictionary:
        while n>=i[1]:
            s=s+i[0]*int(n/i[1])
            n=n % i[1]
     
    for n in range(2,len(dictionary)):
        s=s.replace(dictionary[n][0]*4,dictionary[n][0]+dictionary[n-1][0])

    return s

read(s)

write(3741)
