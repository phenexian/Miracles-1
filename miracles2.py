# Filename: miricales2.py
import random, math

def randomag():
    res=1
    a=1
    while a>0.1:
        res=res*(2.5*random.random()+0.1)
        a=random.random()
    res=res+random.random()*7
    length=int(math.log10(res))
    loosedigits=length-1
    res=round(res,-loosedigits)

    return round(res,1)

def listgram(lst):
    if len(lst)==1:
        return lst[0]
    n=1
    nmax=len(lst)
    ans=lst[0]
    while n<nmax:
        if n==nmax-1:
            ans=ans+" and "+lst[n]
        else:
            ans=ans+", "+lst[n]
        n=n+1
    return ans

def isare(plr):
    if plr==0:
        return "is"
    elif plr==2:
        return "is"
    else:
        return "are"

def itstheir(plr):
    if plr==1:
        return "their"
    else:
        return "it's"

def havehas(plr):
    if plr==1:
        return "have"
    else:
        return "has"

def itthey(plr):
    if plr==0:
        return "it"
    elif plr==2:
        return "it"
    else:
        return "they"

def Itthey(plr):
    if plr==0:
        return "It"
    elif plr==2:
        return "It"
    else:
        return "They"

def invs(word, plr):
    if plr==0:
        word=word+"s"
    return word

def s(word,plr):
    if plr==1:
        word=word+"s"
    return word

def interp(ans):
    if ans in ["yes","y","Y","Yes","yeah","1"]: ans=1
    elif ans in ["no","n","N","NO","nah","0"]: ans=0
    else:
        ans=raw_input("Sorry, yes or no(y/n)?: ")
        interp(ans)
    return ans

def splitpower(power,splits):
    split=[]
    for i in range(0,splits-1):
        chunk=random.random()*power
        power=power-chunk
        split.append(round(chunk,1))
    split.append(round(power,1))
    random.shuffle(split)
    return split

def stuffsolid(stuff):
    if stuff in liquid or stuff in gas:
        return random.choice(["The "+material[0]+" flows freely as normal.", "The "+material[0]+" sustains its shape."])
    else:
        return ""


def loyalties(plr):
    loyalties=[" toatally obedient to "+itstheir(plr)+" creator", " free to do as "+itthey(plr)+" "+invs("like",plr)+", but are fond of "+itstheir(plr)+" creator", " aggresive to "+itstheir(plr)+" creator",
           " aggresive to everything", " docile", " focused on a single task, set when the spell is cast", " inherently evil", " virtuous and kind",
           " obedient to "+itstheir(plr)+" creator for "+str(randomag()+5)+" minutes, after which "+itthey(plr)+" "+random.choice(["rebel against "+itstheir(plr)+" creator", "become docile", "attempt to escape "+itstheir(plr)+" creator"])]
    
    return random.choice(loyalties)

def target(source, cap):
    typ=random.choice(types)
    a=random.random()
    m2=randomag()
    if a>0.7:
        targets="all "+typ+" within "+str(m2+1)+" metres of the "+source
        plr=1
    elif a>0.2:
        typ=typ.replace("ies","y",len(typ)-5)
        typ=typ.replace("s","",len(typ)-1)
        if typ=="ummoned being":
            typ="summoned being"
            
        typ=typ.replace("and","or")
        targets="a chosen "+typ+" within "+str(m2)+" metres of the "+source
        plr=0
    else:
        if source=="item":targets="the user of the item"
        else:targets="the "+source
        plr=0
    if cap==1:
        targets=targets[0].capitalize()+targets[1:]
    return targets, plr

def listconstruct(lst, morethan):
    thelist=[random.choice(lst)]
    a=random.random()
    while a>morethan:
        newitem=random.choice(lst)
        if newitem in thelist:
            a=0
        else:
            thelist.append(newitem)
            a=random.random()

    return listgram(thelist)

def duration(plr, time):
    a=random.random()
    if a>0.9:
        lifetime="forever"
    elif a>0.8:
        lifetime="until "+itthey(plr)+" "+invs("die",plr)
    elif a>0.7:
        lifetime="until "+itthey(plr)+" "+isare(plr)+" exposed to "+random.choice(radiation)
    elif a>0.6:
        lifetime="until "+itthey(plr)+" "+invs("come",plr)+" into physical contact with "+random.choice(stuff)
    else:
        lifetime="for "+str(time)+" hours"

    lifetime=''.join( lifetime )
    return lifetime

def printnice(string):
    string=string.replace("0.0","1")
    string=string.replace(".0","")
    print string

stuff=["fire", "ice", "wood", "granite", "obsidian", "fresh water", "seawater", "blood", "meat", "air", "ash", "glass", "bone", "iron", "bronze",
       "steel", "silver", "gold", "sand", "flesh", "gelatinous ooze", "corrosive acid", "bile", "limestone", "dust", "smoke", "poisonous gas",
       "paper", "mud", "cloth", "lava", "hair","honey","stone", "ivory", "corrosive fumes", "leaves", "cheese", "wax", "crystal", "lace", "plasma",
       "tea", "porridge", "sandstone", "gem stone", "mist", "mercury", "titanium", "aluminium", "platinum", "mould", "diamond", "alcohol", "chitin", "feathers"]
liquid=["fresh water", "seawater", "blood", "gelatinous ooze", "bile", "sand", "corrosive acid", "mud", "lava", "honey", "leaves", "tea", "porridge", "mercury", "feathers"]
gas=["air","fire","smoke", "dust", "poisonous gas", "corrosive fumes", "plasma", "mist"]
shapes=["sphere", "square", "blob", "ring", "collumn", "cage", "wall", "dome", "shard", "pyramid"]
vesels=["lungs", "pots","waterskins", "glasses", "cracks", "scabbards", "cups", "teapots", "flasks", "barrels", "bowls", "chests", "cupboards", "quivers", "helmets", "suits of armour"]
radiation=["moonlight", "sunlight", "torchlight", "light", "darkness", "lightning","unnatural gravitation", "starlight", "wind"]
feelings=["rage", "lust", "calm", "confusion", "fear", "courage", "love", "regret", "amnesia"]
minds=["sentient", "non-sentient", ""]
magnitude=["puny", "slight", "minor", "average", "significant", "strong", "powerful", "extreme", "unbelieveable"]
bodies=["bird", "humanoid", "serpent", "gorilla", "horse", "centaur", "dragon", "ant", "butterfly", "beetle", "bear", "wolf","boar","squid","angel","turtle","cat","fish","shark","lizard","tortoise","pachyderm of the caster's preference", "being inconceivable to the human mind"]
directions=["in all directions", "upwards", "downwards","North","East","South","West","in a chosen direction"]
boosts=["strength", "speed", "stamina", "inteligence", "perceptiveness","coordination"]
props=[["melting point","degrees"],["boiling point","degrees"],["strength","percent"],["weight","percent"],["reflectivity","percent"]]
bodypts=["a pair of arms","a pair of legs","a pair of wings","a bunch of tentacles","a pair of horns","a pair of mandibles","a scorpion tail","a tail","a pair of insectile wings",
         "antlers", "claws","spines","a pair of mantis weapons","a pair of pincers","a bunch of armoured plates","a mane","a turtle-like shell"]
objects=["A chosen object", "The biggest object", "The most valuable object", "The object the caster is looking at"]
timescales=["decades", "years","months","weeks", "days", "hours", "minutes", "seconds"]
sounds=["a deafening boom","an ear splitting scream","the sound of thunder","a mighty roar","a painful screeching sound","an eerie tune","melodic music","a loud pop","a thousand singing choral voices","a pervasive silence","an unearthly sound","a brief whooshing sound","the sound of keys scraping on piano wire"]
colours=["white","black","grey","red","blue","yellow","green","purple","orange","magenta","pink","cyan","turquise","gold-coloured","silver-coloured","transparent","invisible"]
triggers=["destroyed", "brandished", "exposed to "+random.choice(radiation), "touched by "+random.choice(stuff),"looked at",
          "intentionally used by anyone holding it", "intentionally used by its crerator holding it", "touched by a "+random.choice(colours)+" object"]
things=["sword","spear","axe","dagger","arrow","bow","cross-bow","firearm","mace","lance","weapon","hilt","cup","orb","teapot","flask","flower","rake","spade","knife","wig","hat","belt",
        "ring","crown","shoe","glove","fruit","fork","vegetable","table","helmet","book","carpet","key","pot","scabbard","quiver",
        "waterskin","bowl","torch","lamp","candle","rope","boulder","pitchfork","cloak","belt","bird","human","serpent","ape","horse","centaur",
        "dragon","ant","butterfly","beetle","bear", "wolf", "dog","boar","squid","angel","turtle","cat","fish","shark","lizard","tortoise",
        "bat", "insect","frog","pachyderm"]
livingthings=["bird", "human","serpent","ape","horse","centaur","dragon","ant","butterfly","beetle","bear","wolf","dog","boar","squid"
              ,"angel","turtle","cat","fish","shark","lizard","tortoise","pachyderm","bat","insect","frog"]
plants=["blades of grass","daisies","oak trees","pine trees","willow trees","palm trees","roses","elm trees","nettles","bushes","vines","sunflowers","cactai","thistles","mushrooms","liles"]
threats=["kinetic impacts", "high temperatures", "low temperatures", "poison", "acid", "starvation", "thirst", "disease", "intentional attacks","accidents", "bad luck", "anything", random.choice(things)+"s", random.choice(stuff)]
ailments=[random.choice(colours)+" boils", random.choice(colours)+" rashes", "vomiting", "diarrhea","victims' teeth to fall out","headaches","disoreintation","exhaustion",
          "hair loss", "infertility", "pregnancy","coughing"]
types=["allies", "enemies", "humans", "humanoids", "animals", "summoned beings", "humans and anmials","undead beings","animated objects",random.choice(livingthings)+"s"]
spells=["create","transfigure","fill","emotion","summon","transform","protect", "radiate","necro","hyperspell",
        "negate","heroup","detonate","item","delay","portal","temp","properties","sprout","mechro",
        "forced","transfigure2","blast","transfigure3","weather","ethereal","mindmatter","recolour","disease","flash",
        "controled","manipulate","age","garden","unknown","link","uncertain"]

metaspells=["hyperspell","item", "delay","forced"]

catagory=[stuff, radiation, minds, types, bodypts, vesels]


def summon(power, scource):
    split=splitpower(power, 3)
    quantity, length, lifetime=round(split[0],0),split[1],split[2]
    
    madeof=random.choice(stuff)
    bodyshape=random.choice(bodies)
    if quantity<=1:
        thing="creature"
        plr=0
        last="lasts"
        summon=random.choice(["through a portal that snaps shut behind it","via instantaneous appearance", "by disolving into existance"])
    else:
        thing="creatures"
        plr=1
        last="last"
        summon=random.choice(["through portals that snap shut behind them","via instantaneous appearance", "by disolving into existance"])

    lifetime=duration(plr, lifetime)


    addlimbs=listconstruct(bodypts, 0.6)
        
    a=random.random()
    if a>0.5 and len(addlimbs)!=0:
        newstuff=random.choice(stuff)
        addon=" and "+itthey(plr)+" "+havehas(plr)+" "+addlimbs+", made of "+newstuff
    elif len(addlimbs)!=0:
        addon=" and "+itthey(plr)+" "+havehas(plr)+" "+addlimbs
    else:
        addon=""
    
    return "Summons "+str(quantity)+" "+thing+","+itthey(plr)+" "+isare(plr)+" in the shape of a "+bodyshape+" and "+isare(plr)+" made of "+madeof+""".
"""+Itthey(plr)+" "+isare(plr)+" "+str(length)+" meters long"+addon+""".
"""+Itthey(plr)+" "+isare(plr)+" summoned "+summon+", within "+str(randomag())+" meters of the "+scource+". Once summoned "+itthey(plr)+" "+last+" "+str(lifetime)+""".
The """+thing+" "+isare(plr)+loyalties(plr)+"."

def transform(power, source):
    split=splitpower(power, 3)
    quantity, length, lifetime=round(split[0],0),split[1],split[2]
    madeof=random.choice(stuff)
    bodyshape=random.choice(bodies)
    targets, plr=target(source,0)
    
    lifetime=random.choice(["This effect lasts "+duration(plr, lifetime), Itthey(plr)+" may turn back at will"])
  
    a=random.random()
    addlimbs=[]
    while a>0.5:
        newlimb=random.choice(bodypts)
        while newlimb in addlimbs:
            newlimb=random.choice(bodypts)
        addlimbs.append(newlimb)
        a=random.random()
        
    a=random.random()
    if a>0.5 and len(addlimbs)!=0:
        newstuff=random.choice(stuff)
        limbs=listgram(addlimbs)
        addon=" and "+itthey(plr)+" "+havehas(plr)+" "+limbs+", made of "+newstuff
    elif len(addlimbs)!=0:
        limbs=listgram(addlimbs)
        addon=" and "+itthey(plr)+" "+havehas(plr)+" "+limbs
    else:
        addon=""
        
    return "Transforms "+targets+" into "+s("creature",plr)+","+itthey(plr)+" "+isare(plr)+" in the shape of a "+bodyshape+" and "+isare(plr)+" made of "+madeof+""".
"""+Itthey(plr)+" "+isare(plr)+" "+str(length)+" meters long"+addon+""".
"""+str(lifetime)+"."

def create(power, source):
    material=random.choice(stuff)
    shape=random.choice(shapes)
    split=splitpower(power,2)
    return "In a "+shape+" shaped volume of width "+str(split[0])+" metres, "+material+" apears. This is centred at any point within "+str(2*split[1])+" metres of the "+source+"."

def transfigure(power, source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    from1=listconstruct(stuff,0.75)
    
    to=random.choice(stuff)
    while to in from1:
        to=random.choice(stuff)

    shape=random.choice(shapes)

    return "In a "+shape+" shaped volume of width "+str(m1)+" metres, all "+from1+" is turned to "+to+". This is centred at any point within "+str(m2)+" metres of the "+source+"."

def fill(power, source):
    fills=random.choice(vesels)
    fills=fills.split("-")[0]
    material=random.choice(stuff)
    return "All "+fills+" are filled with "+material+" within "+str(power)+" metres of the "+source+"."

def emotion(power, source):
    split=splitpower(power,4)
    m1,m2,m3,m4=split[0],split[1],split[2],split[3]
    feeling=random.choice(feelings)
    mindtype=random.choice(minds)
    m1=round(m1,0)
    if m4>8:m4=8
    mag=magnitude[int(m4)]
    return "All "+mindtype+" beings expirience "+mag+" "+feeling+" for "+str(m3+5)+" minutes, within "+str(m2)+" metres of the "+source+"."

def protect(power, source):
    a=random.random()
    protection=random.choice(threats)
    split=splitpower(power,2)
    m1,m2=split[0],split[1]

    if protection in ["thirst", "starvation", "disease"]:
        timescale=" hours"
    else:
        timescale=" minutes"
        
    targets,plr=target(source,1)
        
    return targets+" "+invs("become",plr)+" imune to harm or pain as a result of "+protection+" for "+str(m2+5)+timescale+"."

def detonate(power,source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    a=random.random()
    if a>0.5:
        detonation="an explosion"
        madness=""
    elif a>0.2:
        detonation="an implosion"
        madness=""
    else:
        madness=random.choice(["gravity to reverse", "space to fold in on itself", "a wormhole to another dimension to open", "time to freeze", "space to be removed from reality and enclosed in its own pocket dimension","all objects to be mirror imaged through their vertical axis"])
        detonation="a disruption in the laws of physics causing "+madness+" for "+str(randomag()+5)+" "+random.choice(timescales)+" in an area"
    return "There is "+detonation+" of radius "+str(m1+1)+" metres centred at a chosen point within "+str(m2+1)+" metres of the "+source+"."

def portal(power,source):
    split=splitpower(power,3)
    m1,m2,m3=split[0],split[1],split[2]
    a=random.random()
    if a>0.7:
        return "A portal of radius "+str(m1+0.2)+" metres appears conecting two points seperated by a distance of up to "+str(2*m2+1)+""" metres.
Both ends of the portal must lie within """+str(m3+(2*m2+1))+" metres of the "+source
    elif a>0.4:
        targets=["The caster is", "All "+random.choice(types)+", within "+str(m2)+" metres, are", random.choice(objects)+" within "+str(m2)+" metres is"]
        target=random.choice(targets)
        return target+" teleported instantly to a chosen area within "+str(m1+m3)+" metres of the "+source
    elif a>0.2:
        targets=["The "+source+" is", "All "+random.choice(types)+", within "+str(m2)+" metres, are", random.choice(objects)+" within "+str(m2)+" metres is"]
        target=random.choice(targets)
        if target==targets[1]:plr=1
        else:plr=0
        return target+" accelerated instantly to "+str(3*m1)+" meters per second towards a chosen point. On reaching that point "+itthey(plr)+" "+invs("stop",plr)+" imediatly."
    else:
        targets=["The caster is", "All "+random.choice(types)+", within "+str(m2)+" metres, are", random.choice(objects)+" within "+str(m2)+" metres is"]
        target=random.choice(targets)
        if target==targets[1]:plr=1
        else:plr=0
        return target+" moved to an empty universe, containing nothing but "+random.choice(colours)+" void above, and an infite "+random.choice(colours)+" plane floor. Each meter "+itthey(plr)+" "+invs("move",plr)+" through this realm corresponds to "+str(m1)+" meters in the real world, while each minute "+itthey(plr)+" "+invs("spend",plr)+" in this world relates to "+str(m3)+" minutes in the real world. "+Itthey(plr)+" "+invs("return",plr)+" to the real world after "+str(randomag())+" minutes of time in the other realm."

def radiate(power,source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    emision=random.choice(radiation)
    a=random.random()
    m1=round(m1,0)
    if m1>8:m1=8
    mag=magnitude[int(m1)]
    direction=random.choice(directions)
    
    if a>0.5:
        targets="the "+source
    else:
        targets="a target point in "+str(m1)+" metres of the "+source
    return "Causes the emision of "+mag+" "+emision+" "+direction+" for "+str(m2+5)+" minutes, from "+targets+"."

def necro(power,source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
 
    a=random.random()    
    if a>0.6:
        targets="All corpses within "+str(m1)+" metres of the "+source
        plr=1
    else:
        targets="A chosen corpse within "+str(m1)+" metres of the "+source
        plr=0

    lifetime=duration(plr, m2)

    a=random.random()
    if a>0.75:
        loyalty=" toatally obedient to "+itstheir(plr)+" creator"
    else:
        loyalty=loyalties(plr)
    
    deadtype=random.choice(["zombies", "ethereal ghosts which are banished on contact with "+random.choice(radiation)])

    return targets+" "+isare(plr)+" reanimated as "+deadtype+", "+itthey(plr)+" "+isare(plr)+loyalty+" , they remain animated "+str(lifetime)+"."

def mechro(power,source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
        
    a=random.random()
    typ=random.choice(["statue", "painting", "reflection", "shadow", random.choice(things),random.choice(things)])

    if a>0.6:
        plr=1
    else:
        plr=0

    if typ in livingthings:
        if typ in ["fish", "shark"]:
            levitate=" and "+itthey(plr)+" can move via levitation"
        else:
            levitate=""
        if plr==1:typ="effigies of "+typ
        else:typ="an effigy of "+typ
    elif typ in things:
        levitate=" and "+itthey(plr)+" can move via levitation"
    else:
        levitate=""
    
    if plr==1:
        targets="All "+typ+"s within "+str(m1)+" metres of the "+source
    else:
        targets="A chosen "+typ+" within "+str(m1)+" metres of the "+source
        
    a=random.random()
    if a>0.75:
        loyalty=" toatally obedient to "+itstheir(plr)+" creator"
    else:
        loyalty=loyalties(plr)

    lifetime=duration(plr, m2)

    return targets+" "+isare(plr)+" animated"+levitate+". "+Itthey(plr)+" "+isare(plr)+loyalty+" , "+itthey(plr)+" "+invs("remain",plr)+" animated "+str(lifetime)+"."

def negate(power,source):
    a=random.random()
    if a>0.7:
        typ=[random.choice(["undead being", "animated object", "summoned creature"])]
        a=random.random()
        while a>0.5:
            a=random.random()
            new=random.choice(["undead being", "animated object", "summoned creature",])
            if new not in typ:
                typ.append(new)
            else:
                a=0
            
        a=random.random()
        if a>0.6:
            for i in typ:
                i=i+"s"
            typ=listgram(typ)
            targets="all "+typ+"s within "+str(power)+" metres of the "+source
        else:
            typ=listgram(typ)
            typ=typ.replace("and","or")
            targets="a chosen "+typ+" within "+str(power)+" metres of the "+source

        return "Effected "+typ+"s are deanimated, they drop lifeless. This effects "+targets

    elif a>0.3:
        split=splitpower(power,2)
        m1,m2=split[0],split[1]
        a=random.random()
        if a>0.6:
            targets="all miracles the effects of which lie entirely within "+str(m2+m1)+" metres "
        else:
            targets="a chosen miracle the effect of which reaches within "+str(m1)+" metres "

        return """Target miracles are negated, their effects instantly cease, anything created by them vanishes and anything transfigured by them reverts to its origional material.
This effects """+targets

    else:
        split=splitpower(power,2)
        m1,m2=split[0],split[1]
        a=random.random()
        if a>0.75:
            if source=="item":targets="if the targets name is written on the items surface in the next few minutes"
            else:targets="if the "+source+" knows the name of the person they wish to target"
        elif a>0.5:
            targets="if the target lies within "+str(m1+1)+" metres of the "+source+"."
        elif a>0.25:
            if source=="item":targets="if the target is pointed at by the item."
            else:targets="if the target can be seen by the "+source+"."
        else:
            if source=="item":targets="if the effects of a miracles caused by the target touch the item."
            else:targets="if the effects of a miracle caused by the target can be seen by the "+source+"."

        return "A target individual looses the ability to see and trigger miracles for "+str(m2+5)+""" minutes.
This only works """+targets

def heroup(power,source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    
    typ=random.choice(types)
    a=random.random()
    targets, plr=target(source,1)
    m1=round(m1,0)
    if m1>8:m1=8
    mag=magnitude[int(m1)]
    boost=random.choice(boosts)

    return targets+" "+invs("expeirence",plr)+" a "+mag+" increase in their "+boost+", for "+str(m2+1)+" minutes."

def temp(power, source):
    split=splitpower(power,3)
    m1,m2, m3=split[0],split[1],split[2]
    shape=random.choice(shapes)
    direction=random.choice(["increases by","decreases by","becomes"])
    return "In a "+shape+" shaped region of width "+str(m1+1)+" metres, the tempertature "+direction+" "+str(10*m2)+" degrees (celcius). This is centred at a point in "+str(m3)+" metres of the "+source

def properties(power, source):
    split=splitpower(power,3)
    m1,m2, m3=split[0],split[1],split[2]
    from1=listconstruct(stuff,0.75)

    thing=random.choice(props)
    direction=random.choice(["increased", "decreased"])
    shape=random.choice(shapes)
    return "All "+from1+" in a "+shape+" shaped region of width "+str(m1+0.5)+" metres has its "+thing[0]+" "+direction+" by "+str(10*m2)+" "+thing[1]+". This is centred at a point in "+str(m3)+" metres of the "+source+"."

def sprout(power, source):
    part=random.choice(bodypts)
    
    targets,plr=target(source,1)
    a=random.random()
    if a>0.4:
        made=""
        extra1=""
    else:
        a=random.random()
        if a<0.5:
            extra1=", they"+" are mobile and animated"
        else:
            extra1=", they"+" are imobile and inanimate"
            
        material2=random.choice(stuff)
        made="made of "+material2+". "+stuffsolid(stuff)
    targets=targets.replace("and","or")
        
    return targets+" "+invs("grow",plr)+" "+part+" "+made+" They last "+str(power)+" minutes"+extra1+"."

def transfigure2(power, source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    a=random.random
    if a>0.3:
        material1=random.choice(types)
    else:
        material1=random.choice(bodies)+" shaped creatures"
    m1=(m1/2)+0.5

    shape=random.choice(shapes)

    a=random.random()
    if a<0.5:
        extra1=" They"+" remain mobile and animated"
    else:
        extra1=" They"+" are no longer animated"

    material2=random.choice(stuff)
    made=material2+". "+stuffsolid(stuff)
    
    return "In a "+shape+" shaped volume of width "+str(m1)+" metres within "+str(m2)+" meters of the "+source+", all "+material1+" are turned to "+made+extra1+"."

def blast(power, source):
    split=splitpower(power,3)
    m1,m2,m3=round(split[0],0),split[1],split[2]

    if m1<=1:
        plr=0
    else:
        plr=1

    a=random.random()
    if a>0.5:
        material=random.choice(stuff)
        made,extra="made of "+material,stuffsolid(stuff)
    else:
        made,extra="",""

    return "Fires "+str(m1)+" "+s(random.choice(things),plr)+" "+made+" at "+str(3*m2)+" metres per second, away from the "+source+". "+extra+Itthey(plr)+" "+invs("fade",plr)+" away after "+str(m3)+" minutes."
    
def transfigure3(power, source):
    thing1=listconstruct(things,0.9)
    thing2=random.choice(things)

    while thing2 in thing1:
        thing2=random.choice(things)

    a=random.random()
    if a>0.75:
        material=random.choice(stuff)
        made=" made of "+material+". "+stuffsolid(stuff)
    else:
        made=""

    a=random.random()
    if a>0.5:
        return "All "+thing1+"s whithin "+str(power+1)+" meters of the "+source+" are turned into "+thing2+"s"+made+"."
    else:
        a=random.random()
        if a>0.75:
            spell=random.choice(spells)
            power=power*random.random()*2
            exec("ans="+spell+"(power,thing2)")
            ans="The "+thing2+""" has the property that each time it is activated:
    """+ans+"""
It is activated whenever """+random.choice(triggers)+"."
        else:
            ans=""
        thing1=thing1.replace(" and "," or ")
        return "A chosen "+thing1+" within "+str(power)+" metres of the "+source+" is turned into a "+thing2+made+""".
"""+ans
    
def weather(power,source):
    a=random.random()
    if a>0.5:
        state=random.choice(["cloudy", "rainy", "misty", "sunny", "windy"])

        mag=random.choice([" slightly ", " ", " very "])
        return "The weather instantly becomes"+mag+state+" in the area surrounding the "+source
    elif a>0.4:
        colour=random.choice(colours)
        return "In the area surrounding the "+source+" the sky becomes "+colour+", to observers outside this area it appears unchagned, and the effects fade as one leaves the area. The re-clouring lasts a few hours."
    elif a>0.2:
        state=random.choice(["thunderstorm", "earthquake", "tornado", "comet strike"])
        return "This causes a "+random.choice(magnitude)+" "+state+" in the area surrounding the "+source
    else:
        return "This causes it to rain "+random.choice(stuff)+" for "+str(power+10)+" minutes, in the area surrounding the "+source+"."
    
def ethereal(power, source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    effect=random.choice(["ethereal","invisible",random.choice(["half", "twice", "ten times", "a tenth"])+" as large"])
    a=random.random()
    if a>0.5:
        if a>0.75:
            target=random.choice(things)+"s"
        else:
            target=random.choice(types)
        return "All "+target+" within "+str(m2+1)+" metres of the "+source+" become "+effect+" for "+str(m1+0.1)+" minutes."

    else:
        if a>0.25:
            target="object"
        else:
            target=random.choice(things)
        return "A chosen "+target+" within "+str(m2+1)+" meters of the "+source+" with a mass no greater than "+str(m1*2)+" kilos becomes "+effect+"."

def mindmatter(power, source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    targets,plr=target(source,1)
    way=random.choice(["using their "+s("mind",plr), "using hand gestures", "by commanding it verbally", "by playing musical instruments (it dances to "+itstheir(plr)+" tunes)"])
    from1=listconstruct(stuff,0.75)
    return targets+" "+invs("gain",plr)+" the ability to control "+from1+" within "+str(m1)+" metres of themselves "+way+". This lasts for "+str(m2)+" minutes."

def recolour(power, source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    froms=listconstruct(colours,0.5)

    to=random.choice(colours)
    while to in froms:
        to=random.choice(colours)

    return "Everything "+froms+" within "+str(m1)+" meters of the "+source+" becomes "+to+" for "+str(m2)+" "+random.choice(timescales)+"."

def disease(power,source):
    targets,plr=target(source,0)

    effects=listconstruct(ailments,0.5)

    if "pregnancy" in effects:
        extra="If any beings (male or female) who become pregnant from this ailment give birth then the child will be the shape of a "+random.choice(bodies)+", they will be of normal size and inteligance for their parents species."
    else:extra=""
    
    contag=random.choice(["contagous by touch", "contagous through the air", "contagous through eye contact", "not contagous at all", "contagous via intercourse",
                         "contagous by verbal comunication","contagous through written comunication", "contagous by contact with infected blood","instantly contracted by infected individual's descendants","instantly contracted by infected individuals ancestors and siblings","it is contagous by thought (thinking about individuals who have it will result in catching it)"])

    cure=random.choice(["a good nights sleep", "a few days rest", "strenuous exercise","hot tea", "medicinal herbs", "bloodletting with leeches", "true loves first kiss",
                        "infecting somone else with it", "praying", "nothing", "waiting a few hours", "contact with "+random.choice(radiation), "consuming some "+random.choice(stuff),])

    
    return "A new disease is brought into existance, it's first "+s("victim",plr)+" "+isare(plr)+" "+targets+""".
The disease causes """+effects+". It is "+contag+". It can be cured by "+cure+"."+extra

def manipulate(power, source):
    split=splitpower(power,3)
    m1,m2,m3=split[0],split[1],split[2]
    a=random.random()
    if a>0.6:
        manipulated="levitate up to "+str(m1+1)+" kilos of "+random.choice(stuff)+" and move it freely in any direction"
    elif a>0.2:
        manipulated="levitate up to "+str(m1+1)+" kilos of "+random.choice(stuff)+" and manipulate it with precision"
    else:
        manipulated="levitate all "+random.choice(things)+"s and move them freely in any direction"
    if source=="item":
        self="user of the item"
    else:
        self=source
    return "For the next "+str(randomag()+5)+" minutes the "+self+" can "+manipulated+" at a maximum speed of "+str(m3)+" metres per second, within "+str(3*m2)+" metres"

def age(power, source):
    a=random.random()
    if a>0.5:
        targets, plr=target(source, 1)
    else:
        targets="All "+random.choice(things)+"s within "+str(randomag())+" meters of the "+source
        plr=1
    direction=random.choice(["increased","decreased"])

    a=random.random()
    if a>0.8:
        return targets+" will from now on "+random.choice(["age at twice the rate","age at half the rate","not age at all","grow younger at a rate of 1 year per year","have an age that varies in proportion to their latitude"])+"."
    else:
        return targets+" "+havehas(plr)+" "+itstheir(plr)+" phyical age "+direction+" by "+str(power)+" years."

def garden(power, source):
    plant=random.choice(plants)
    adject=random.choice(["carnivorous","stinging ","posionous", "dead", random.choice(colours), "","bonsai","pleasant smelling","fruit bearing","magnetic","fully mobile and sentient"])
    if adject=="fully mobile and sentient":
        addon="They are"+loyalties(1)
    else:
        addon=""
    appear=random.choice(["burst from the ground","pop into existance", "grow rapidly out of the ground", "appear through portals that snap shut behind them"])

    a=random.random()
    if a>0.8:
        when=""
    elif a>0.6:
        when="When the "+plant+" are burned "+random.choice(["their combustion emits cold, not heat","the flames are "+random.choice(colours),"the smoke is "+random.choice(colours),"they scream","they sing"])+"."
    elif a>0.4:
        effect=random.choice(["they cause halucinations","they are medicinal","they are negativly nourishing (meaning that their consumption acceletates starvation)","they are highly addictive","they have a calming effect","manipulate"])
        if effect=="manipulate":
            exec("""effect=manipulate(power, "the consumer")""")
            effect=effect.lower()
        when="When the "+plant+" are consumed "+effect+"."
    elif a>0.2:
        when="When dew gathers on the "+plant+" the dew "+random.choice(["glows "+random.choice(colours),"is medicinal","is negativly thirst quenching (meaning that drinking it accelerates death from thrist)","is acidic","is poisonous","is made of "+random.choice(liquid),"is highly flamable","is hundreds of kilos per drop in weight"])
    else:
        effect=random.choice(["they turn "+random.choice(colours),"they explode","they implode","they glow "+random.choice(colours),"they transform into "+random.choice(things)+"s"])
        when="When the "+plant+" are exposed to "+random.choice(radiation)+" "+effect+"."

    return "Within a "+str(power)+" meter radius of the "+source+" "+adject+" "+plant+" "+appear+". "+when

def link(power,source):
    split=splitpower(power,2)
    m1,m2=split[0],split[1]
    if source=="object":
        thing="user of the object"
    else:
        thing=source
    targettypes=["animal","human","ally","enemy","sentient being"]
    targetables=["the "+thing,"the "+thing+"'s first love","the "+thing+"'s greatest living enemy","the "+thing+"'s oldest parent (or creator)"]
    for i in targettypes:
        targetables=targetables+["a target "+i+" within "+str(m1)+" meters of the "+source,"the "+i+" nearest to the "+source]
    random.shuffle(targetables)
    t1,t2=targetables[0],targetables[1]

    effect=random.choice(["swap bodies (each of them finds themselves piloting the others body)","become mindlinked (they are able to comunicate mind to mind, and make use of one anothers senses)","become lifelinked (the death of either of them will result in the death of both)","are fused together mind body and soul","are each teleported to the others position (swap places)"])
    t1=t1[0].capitalize()+t1[1:]

    return t1+" and "+t2+" "+effect+". This lasts "+duration(1,m2).replace("they",random.choice(["either of them","both of them simultaneously"]))+"."
    
def delay(power,source):
    m3=randomag()
    spell=random.choice(spells)
    while spell in metaspells:
        spell=random.choice(spells)
        m3=m3+randomag()
    exec("ans="+spell+"(power, source)")
    ans="After activation their is a "+str(m3+1)+""" minute delay before the following effect occurs:
    """+ans
    return ans

def item(power, source):
    split=splitpower(power,5)
    m1=split[0]
    power=power-m1

    source2="object"
    spell=random.choice(spells)
    while spell=="forced":
        spell=random.choice(spells)
    exec("ans="+spell+"(power,source2)")

    ans=random.choice(objects)+" within "+str(m1)+" metres of the "+source+""" gains the property such that each time it is activated:
    """+ans+"""
It is activated whenever """+random.choice(triggers)
    return ans

def hyperspell(power,source):
    spell=random.choice(spells)
    power=power+1000
    exec("ans="+spell+"(power,source)")

    for i in magnitude:
        if i in ans:
            ans=ans.replace(i,"unbelievable")
            
    n=2
    while n<len(timescales)-1:
        if timescales[n] in ans:
            ans=ans.replace(timescales[n],timescales[n-2])
        n=n+1
    n=0
    at=0
    for i in range(1,9):
        pt=ans.replace(str(i)+".",str(i)+"0.")
        pt=ans.replace(str(i)+" ",str(i)+"0")
        
    return """This miracle is extremely powerful, it can only be negated by another extremely powerful miracle.
    """+ans

def flash(power,source):
    spell=random.choice(spells)
    exec("ans="+spell+"(power, source)")
    ans=ans+"\nThis miracles activation is occompanied by a "+random.choice(magnitude)+random.choice([" flash of "+random.choice(colours)+" light"," blast of wind"," swirling "+random.choice(colours)+" aura."," discharge of "+random.choice(colours)+" sparks."])

    a=random.random()
    if a>0.5:
        ans=ans+" and "+random.choice(sounds)+"."
    else:
        ans=ans+"."

    return ans
    
def forced(power, source):
    spell=random.choice(spells)
    while spell in metaspells:
        spell=random.choice(spells)
    exec("ans="+spell+"(power, source)")
    ans="""The following miracle must be activated, it is imposible to not use it:
    """+ans
    return ans

def controled(power, source):
    spell=random.choice(spells)
    while spell=="controled":
        spell=random.choice(spells)
    exec("ans="+spell+"(power, source)")
    if source=="object":source="user of the object"
    return "The "+source+""" has a high degree of control over the following miracle, as it occurs they may reduce any of it's magnitudes by as much as they desire.
"""+ans

def unknown(power,source):
    spell=random.choice(spells)
    while spell=="unkown" or spell=="uncertain" or spell=="unknown":
        spell=random.choice(spells)
    exec("ans="+spell+"(power, source)")
    Do=interp(raw_input("The effects of this miracle are impossible to predict, would you like to set it of anyway?(y/n):"))
    if Do==1:
        return ans
    else:
        return ""

def uncertain(power,source):
    spell=random.choice(spells)
    while spell=="unkown" or spell=="uncertain" or spell=="forced":
        spell=random.choice(spells)
    exec("ans="+spell+"(power, source)")

    ansdisplay=ans

    for i in things+stuff+types+radiation+feelings+vesels+bodypts+colours+threats+ailments:
        ansdisplay=ansdisplay.replace(" "+i+" "," * ")

    for i in range(0,9):
        for g in [".",""]:
            ansdisplay=ansdisplay.replace(str(i)+g,"*")

    while "**" in ansdisplay:
        ansdisplay=ansdisplay.replace("**","*")

    print "This miracles overal nature can be determined, but some details are hidden. The *'s show uncertainties:\n"+ansdisplay+"\n"
    Do=interp(raw_input("Would you like to set off this miracle?(y/n):"))
    if Do==1:
        return ans
    else:
        return ""

def miracle():
    power=randomag()
    spell=random.choice(spells)
    source="caster"
    exec("ans="+spell+"(power, source)")
    if "all" or "All" in ans:
        power=power*3
    add="\nThis miracle has an overall power of "+str(power)+"."
    return ans+add


for i in range(0,5):
    printnice(miracle())
    print "\n"

done=raw_input("Are you done?:")
