import csv

trial1=open("trial1.csv")
t1=csv.reader(trial1)
U1sM=[]
for row in t1:
    ls=row
    U1sM.append(float(ls[1]))
trial1.close()


trial2=open("trial2.csv")
t2=csv.reader(trial2)
U2sM=[]
for row in t2:
    ls=row
    U2sM.append(float(ls[1]))
trial2.close()


trial3=open("trial3.csv")
t3=csv.reader(trial3)
U3sM=[]
for row in t3:
    ls=row
    U3sM.append(float(ls[1]))
trial3.close()


trial4=open("trial4.csv")
t4=csv.reader(trial4)
U4sM=[]
for row in t4:
    ls=row
    U4sM.append(float(ls[1]))
trial4.close()


trial5=open("trial5.csv")
t5=csv.reader(trial5)
U5sM=[]
for row in t5:
    ls=row
    U5sM.append(float(ls[1]))
trial5.close()


trial6=open("trial6.csv")
t6=csv.reader(trial6)
U6sM=[]
for row in t6:
    ls=row
    U6sM.append(float(ls[1]))
trial6.close()


print(len(U1sM))
print(len(U2sM))
print(len(U3sM))
print(len(U4sM))
print(len(U5sM))
print(len(U6sM))
