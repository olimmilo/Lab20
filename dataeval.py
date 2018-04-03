import csv
import numpy

"""
Experiment vars which could be input but are just written into the code are defined at the top in all caps

smoothing function was provided in the scipy numpy handbook and is not my own work
"""
HOTWATERMASS=[47.566,39.409,50.068,45.215,50.995,51.541]
COLDWATERMASS=[50.240,49.317,50.120,48.420,59.995,49.905]
HOTWATERTEMP=[95,93,94,92,95,89]


def smooth(list,degree=3):

    window=degree*2-1

    weight=numpy.array([1.0]*window)

    weightGauss=[]

    for i in range(window):
        i=i-degree+1
        frac=i/float(window)
        gauss=1/(numpy.exp((4*(frac))**2))
        weightGauss.append(gauss)

    weight=numpy.array(weightGauss)*weight
    smoothed=[0.0]*(len(list)-window)

    for i in range(len(smoothed)):
        smoothed[i]=sum(numpy.array(list[i:i+window])*weight)/sum(weight)

    return(smoothed)


def sum(list):
    i = 0
    s = 0
    while i < len(list):
        s += list[i]
        i += 1
    return(s)


def mean(list):
    i = 0
    s = sum(list)
    mean = s/len(list)
    return(mean)


def LinReg(list,x0):
    y=list
    x=[]
    while len(x) <= len(y)+x0:
        x.append(len(x)+x0)
    xy=[n*m for n,m in zip(x,y)]
    x2=[j**2 for j in x]
    n=len(list)
    m=((n*sum(xy))-(sum(x)*sum(y)))/((n*sum(x2))-(sum(x)**2))
    b=(sum(y)-(m*sum(x)))/n
    ans=[m,b]
    return(ans)


def LineInt(LINEONE, LINETWO):
	x1=0
	x2=0
	y1=LINEONE[1]
	y2=LINETWO[1]
	m1=LINEONE[0]
	m2=LINETWO[0]
	COOR=[((((m1*((m2*(x1-x2))+y2))-(y1*m2))/(m1-m2))-y1+(m1*x1))/m1,(((m1*((m2*(x1-x2))+y2))-(y1*m2))/(m1-m2))]
	return(COOR[1])


def convert(iteration):
    name="trial"+str(iteration)+".csv"
    functrial=open(name)
    funct=csv.reader(functrial)
    funclist=[]
    for row in funct:
        ls=row
        funclist.append(float(ls[1]))
    functrial.close()
    return(funclist)


def SetDivide(list):
    set0=[]
    set1=[]
    set2=[]
    set3=[]

    ##set0
    set0.append(list[0])
    i = 1
    stop = 0
    while stop == 0:
        medbound = mean(list)
        limit = 1
        lowbound = medbound - limit
        highbound = medbound + limit
        temptest=list[i]
        if temptest >= lowbound and temptest <= highbound:
            set0.append(temptest)
        else:
            stop = 1
            setof0=i-1
        i += 1
    stop = 0

    ##set2


    ##set2
    end = 1000
    i=len(list)-end
    while i < len(list):
        set3.append(list[i])
        i += 1

    i=(len(list)-end)-1

    while stop == 0:
        reg=LinReg(set3,i)
        m=reg[0]
        b=reg[1]
        yest= (m*i)+b
        sigma = (yest - list[i])**2
        if sigma < 16:
            set3.insert(0,list[i])
        else:
            stop = 1
            setof2 = i + 1
        i = i-1
    stop = 0

    ##set3
    setof3=len(list)

    ##sumative
    full=[setof0,setof1,setof2,setof3]
    return(full)


def CalCalc(list,breakpts,iteration):
    lin0lis=[]
    lin1lis=[]
    lin2lis=[]
    i=0
    while i < breakpts[0]:
        lin0lis.append(list[i])
        i += 1
    i=breakpts[0]
    while i < breakpts[1]:
        lin1lis.append(list[i])
        i += 1
    i=breakpts[2]
    while i < breakpts[3]:
        lin2lis.append(list[i])
        i += 1
    lin1=LinReg(lin1lis)
    lin2=LinReg(lin2lis)
    peak=LineInt(lin1,lin2)
    deltat=abs(mean(lin0lis)-peak)
    deltathot=abs(HOTWATERTEMP[iteration]-peak)
    deltatcold=abs(mean(lin0lis)-peak)
    deltaqhot=HOTWATERMASS[iteration] * 4.179 * deltathot
    deltaqcold=COLDWATERMASS[iteration] * 4.179 * deltatcold
    calcon=(deltaqhot-deltaqcold)/deltat
    return([mean(lin0lis),peak,calcon])


##work

Trials=[]
i=1

while i < 7:
    Trials.append(convert(i))
    i += 1

i=0
SmoothTrials=[]

while i < len(Trials):
    SmoothTrials.append(smooth(Trials[i]))
    i += 1

i=0
BreakPts=[]
while i < len(SmoothTrials):
    BreakPts.append(SetDivide(SmoothTrials[i]))
    i += 1
"""
i=0
calcon=[]
while i < len(SmoothTrials):
    calcon.append(CalCalc(SmoothTrials[i],BreakPts[i],i))
    i += 1

print(calcon)
"""

##testing
test=SetDivide(SmoothTrials[3])
print(test[0])
print(test[3][0])
