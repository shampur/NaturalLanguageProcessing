__author__ = 'sharan'

f1 = open('data501.txt','r')
f2 = open('output5050.txt','r')
list1=[]
list2=[]
dict1=[]
val1=f1.readlines()
val2=f2.readlines()
if len(val1) == len(val2):
    for val in val1:
        list1.append(val.split(' ')[0])
    for val in val2:
        list2.append(val.split(' ')[0])
    for val in range(len(list1)):
        dict1.append((list1[val],list2[val]))
lis3=[1,2,3,4,5,6]

for val1 in lis3:
    relcount=0
    totalcount=0
    irrcount=0
    for val in dict1:
        if val1 == int(val[0]) and val1 == int(val[1]):
            relcount += 1
        if val1 == int(val[1]):
            totalcount += 1
        if val1 == int(val[0]):
            irrcount += 1
    prec=float(relcount)/totalcount
    rec=float(relcount)/irrcount
    accuracy=(2*prec*rec)/(prec+rec)
    print str(val1) + " " + str(accuracy) + ' ' + str(prec) + ' ' + str(rec)