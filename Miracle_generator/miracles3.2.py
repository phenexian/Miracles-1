# Filename: miricales3.py
import random, math
import listfunctions as lf

store_list=[]

listlist=['stuff','colour','sentences','reach','magnitude','feeling','target','distance','effect','method',
          'trigger','radiation','animal','loyalty','duration','limbs','size','number','shape','thing',
          'twoparty','action','threat','vesel','aperature','aim','ailments','contagious','cure','adjective',
          'animatable','plant','building','stat','chances']

def openthem(filename):
    lst=[]
    with open("lists\\"+filename+".txt", 'r') as s:
        raw_file=s.readlines()
    
    for i in raw_file:
        lst.append(i.rstrip())
    return lst

def snip(sentence,word):
    n=sentence.find(word+"_")
    n=n+len(word)+1
    out=""
    while sentence[n]!="}":
        out=out+sentence[n]
        n=n+1
    return out

def find(lst,function):
    global store_list
    lst=lst[1:-1].replace(function,"")
    for i in listlist:
            if i[0]==lst:
                mylist=i[1]
    if function=="":
        return random.choice(mylist)
    elif function=="land":
        return lf.listconstruct(mylist,1)
    elif function=="lor":
        return lf.listconstruct(mylist,0)
    elif function in ["1","2","3"]:
        try:
            a=store_list[0]
            store_list.remove(a)
            return a
        except:
            store_list=random.sample(mylist,int(function))
            a=store_list[0]
            store_list.remove(a)
            return a

def fancy_cut(sentence):
    kets=["{","}"]
    state=0
    out=[]
    bit=""
    n=0
    while n<len(sentence):
        if sentence[n]=="{":
            state=state+1
            if state==1:
                out.append(bit)
                bit=sentence[n]
            else:
                bit=bit+sentence[n]
                
        elif sentence[n]=="}":
            state=state-1
            if state==0:
                bit=bit+sentence[n]
                out.append(bit)
                bit=""
            else:
                bit=bit+sentence[n]
        else:
            bit=bit+sentence[n]
        n=n+1
    out.append(bit)
    
    return out
        
def go():
    userinput=raw_input("""What would you like to do?
Enter an integer for that many miracles, one after another
Enter a word to get a single miracle containing that word:""")

    if userinput=="":
        userinput=" "

    try:
        n=int(userinput)
        for i in range(0,n):
            print "\n"+"-"*60+"\n"
            print cleanup(miracle())
    except:
        i=0
        mirc=miracle()
        while userinput not in mirc and i<1200:
            mirc=miracle()
            i=i+1
                
        print "\n"+"-"*60+"\n"
        if i<1200:
            print cleanup(mirc)
        else:
            print "The miracles prove ellusive, none are found."
        
    print "\n"+"-"*60+"\n"
    go()


def explicify(sentence):
    sentence=fancy_cut(sentence)

    n=0
    while n<len(sentence)-1:
        if "_" in sentence[n]:
            cut=sentence[n].split("_")
            phrase=find(cut[0]+"}","")
            sentence[n]=phrase.replace("{x}",cut[1][0:-1])
        elif "\\" in sentence[n]:
            cut=sentence[n][1:-1].split("\\")
            sentence[n]=random.choice(cut)
        n=n+1

    for n in ["","land","lor","3","2","1"]:
        sentence = [find(i,n) if i[1:-1].replace(n,"") in zip(*listlist)[0] else i for i in sentence]
         
    sentence = ["caster" if i[1:-1]=="source" else i for i in sentence]
    out_sentence=""
    for i in sentence:
        out_sentence=out_sentence+i
        
    return out_sentence

def cleanup(sentence):
    sentence=sentence.replace("it act","it acts")

    if "it are" in sentence:
        cut=sentence.split("it are")
        cut[1]=cut[1].replace("their","it's")
        sentence=cut[0]+"it is"+cut[1]

    cut=sentence.split(".")
    sentence=""
    for i in cut:
        try:
            if i[0]==" ":
                i=" "+i[1].upper()+i[2:]
            else:
                i=i[0].upper()+i[1:]
        
            sentence=sentence+i+"."
        except:
            sentence=sentence+i
        
    sentence=sentence.replace("..",".")

    return sentence

def miracle():
    i=0
    sentence=find("{sentences}","")
    sentence=sentence.lower()
    while "{" in sentence and i<20:
        sentence=explicify(sentence)
        i=i+1

    return sentence

def test():
    i=0
    mlist=[]
    n=miracle()
    while n not in mlist:
        mlist.append(n)
        n=miracle()
        i=i+1
    print n
    print i
    return i

def bigtest():
    lot=0
    for v in range(1,100):
        lot=lot+test()
    print "\n"
    print (lot/100)

listlist2=[]
yes,no=["{x}"],[""]
for i in listlist:
    listlist2.append([i,openthem(i)])

for n in listlist2:
    if n[0]=="chances":
        for i in n[1]:
            exec("a="+i)
            listlist2.append([a[0],(int(a[1])*yes+int(a[2])*no)])
        listlist2.remove(n)

listlist=listlist2

go()
