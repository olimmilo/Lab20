import csv
import numpy

"""
Experiment vars which could be input but are just written into the code are defined at the top in all caps

smoothing function was provided in the scipy numpy handbook and is not my own work
"""
WATERMASS=[]
SALTMASS=[]
DATALEN=150


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
        funclist.append(float(ls[0]))
    functrial.close()
    return(funclist)
