# Filename: miricales3.py
import random, math
import listfunctions as lf

listlist=['stuff','colour','sentences','reach','magnitude','feeling','target','distance','effect','method',
          'trigger','radiation','animal','loyalty','duration','limbs','size','number','shape','thing',
          'twoparty','action','threat','vesel','aperature','aim','ailments','contagious','cure','adjective',
          'chances']

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

def find(lst):
    for i in listlist:
        if i[0]==lst:
            return i[1]
    return str([lst])

def cleanup(sentence):
    sentence=sentence.replace("_"," ")
    return sentence

def explicify(sentence,source,xs):
    x2=["['0']"]
    form=""
    # This will replcae {}'d values with words from the list they point too

    for x in xs:
        form=form+"random.choice("+str(x)+"),"
    
    for n in listlist:
        i=[str(n[0]),str(n[1])]
        if "{lor"+i[0]+"}" in sentence:
            form=form+"lor"+i[0]+"=lf.listconstruct("+i[1]+",0),"
        elif "{land"+i[0]+"}" in sentence:
            form=form+"land"+i[0]+""+"=lf.listconstruct("+i[1]+",1),"
        elif "{"+i[0]+"}" in sentence:
            form=form+i[0]+"=random.choice("+i[1]+"),"
        else:
            # This exists to deal with multiple inputs of the same type
            for n in ["3","2","1"]:
                if "{"+i[0]+n+"}" in sentence:
                    form=form+i[0]+n+"=lf.differlist("+i[1]+","+n+"),"

            # form {a_b} is read as a but with all instances of {x} in {a} set to b
            if "{"+i[0]+"_" in sentence:
                v=snip(sentence,i[0])
                form=form+i[0]+"_"+v+"=random.choice("+i[1]+"),"
                x2=x2+[find(v)]
                try:
                    x2.remove("['0']")
                except:
                    x2=x2
                    
        if "{tr"+i[0]+"}" in sentence:
            form=form+"tr"+i[0]+"=random.choice("+i[1]+"),"
            
    form=form+"source='"+source+"',"

    exec("sentence=sentence.format("+form+")")

    if "{" in sentence:
        sentence=explicify(sentence,source,x2)
    return sentence

def miracle():
    sentence=random.choice(find("sentences"))
    sentence=explicify(sentence,"caster",["['0']"])
    sentence=cleanup(sentence)
    
    return sentence
 
def go():
    userinput=raw_input("""What would you like to do?
Enter an integer for that many miracles, one after another
Enter a word to get a single miracle containing that word
Enter * to see and edit options:""")

    if userinput=="":
        userinput=" "

    try:
        n=int(userinput)
        for i in range(0,n):
            print "\n"+"-"*60+"\n"
            print miracle()
    except:
        i=0
        mirc=miracle()
        while userinput not in mirc and i<1200:
            mirc=miracle()
            i=i+1
                
        print "\n"+"-"*60+"\n"
        if i<1200:
            print mirc
        else:
            print "The miracles prove ellusive, none are found."
        
    print "\n"+"-"*60+"\n"
    go()

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
yes,no=["{}"],[""]
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
