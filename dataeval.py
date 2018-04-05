import csv
import numpy

"""
Experiment vars which could be input but are just written into the code are defined at the top in all caps

smoothing function was provided in the scipy numpy handbook and is not my own work
"""

##Experiment vars
WATERMASS=[155.190,143.052,155.715,137.885,80.971,144.443]
SALTMASS=[4.975,4.144,4.703,4.545,4.835,4.540]
SHEATWATER=4.186
CALCON=16.2
DATALEN=175
INTERVALS=[1,1,1,1,2,2]

ROWLABELS=["Minimum Temperature","Maximum Temperature","Change in Temperature","Enthalpy"]
COLLUMNLABELS=["___","Nickel Chloride","Sodium Nitrate","Aluminium Nitrate"]

##defines functions

def smooth(list,degree=6):
    return(list)

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


def LinReg(list,start,interval):
    y=list
    x=[]
    while len(x) < len(y):
        x.append((len(x)*interval)+start)
    xy=[n*m for n,m in zip(x,y)]
    x2=[j**2 for j in x]
    n=len(list)
    m=((n*sum(xy))-(sum(x)*sum(y)))/((n*sum(x2))-(sum(x)**2))
    b=((sum(y)*sum(x2))-(sum(x)*sum(xy)))/((n*sum(x2))-(sum(x)**2))
    ans=[m,b]
    return(ans)


def LineInt(lin1, lin2):
	m=lin1[0]
	b=lin1[1]
	n=lin2[0]
	c=lin2[1]
	y=((n*b)-(m*c))/(n-m)
	x=(y-c)/n
	intersect=[x,y]
	return(intersect)


def convert(iteration,datalen,interval):
    name="trial"+str(iteration)+".txt"
    functrial=open(name).readlines()
    funclist=[]
    i=0
    while len(funclist) < datalen:
	funclist.append(float(functrial[i]))
	i += interval
    return(funclist)


def enthalpychange(minl,maxl,iteration):
    m=WATERMASS[iteration]+SALTMASS[iteration]
    s=SHEATWATER
    t=maxl-minl
    q=(m*s*t)+CALCON
    return(q)


def calculations(list,iteration):
    minl=min(list)
    maxl=max(list)
    deltal=maxl-minl
    enthalpy=enthalpychange(minl,maxl,iteration)
    calcs=[minl,maxl,deltal,enthalpy]
    return(calcs)


def finish(m,table):
    avglist=[ROWLABELS[m]]
    i=0
    while i < len(table):
        avglist.append(mean([table[i][m],table[i+1][m]]))
        i += 2
    return(avglist)
##creates smoothed data sets

rawtrials=[]
    
i=0
while i < 6:
    it = i + 1
    rawtrials.append(convert(it,DATALEN,INTERVALS[i]))
    i += 1

smoothtrials=[]

i=0
while i < len(rawtrials):
    smoothtrials.append(smooth(rawtrials[i]))
    i += 1

##preforms calculations
calctable=[]

i=0
while i < len(smoothtrials):
    calctable.append(calculations(smoothtrials[i],i))
    i += 1
i=0

    
fintable=[COLLUMNLABELS]

i=0
while i < 4:
    fintable.append(finish(i,calctable))
    i += 1

i=0
i=0

with open('output.csv','w') as printfile:
    writer = csv.writer(printfile)
    writer.writerows(fintable)

print(fintable)