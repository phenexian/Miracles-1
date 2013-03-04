# Filename: listfunctions.py
import random

def listconstruct(lst,andor):
    thelist=[random.choice(lst)]
    a=random.random()
    while a>0.6:
        newitem=random.choice(lst)
        if newitem in thelist:
            a=0
        else:
            thelist.append(newitem)
            a=random.random()

    return listgram(thelist,andor)

def listgram(lst,andor):
    if len(lst)==0:
        return ""
    elif len(lst)==1:
        return lst[0]
    n=1
    nmax=len(lst)
    ans=lst[0]
    while n<nmax:
        if n==nmax-1:
            if andor==0:
                ans=ans+" or "+lst[n]
            else:
                ans=ans+" and "+lst[n]
        else:
            ans=ans+", "+lst[n]
        n=n+1
    return ans

def differlist(lst,n):
    try:
        if sample[0] in lst:
            a=sample[0]
            sample.remove(a)
            return a
        else:
            sample=[]
            return differlist(lst,n)
    except:
        try:
            sample=random.sample(lst,n)
        except:
            sample=[]
            for i in lst:
                sample.append(i)
            random.shuffle(sample)
        global sample
        return differlist(lst,n)
    
