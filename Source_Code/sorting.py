__author__ = 'sharan'
import operator

w=open('/home/natraj/Downloads/svm/postraining.txt','w')
with open('/home/natraj/Downloads/finalproject/finalTrainFile2.txt','r') as f:
    line=f.readlines()
    for val in line:
        val2 = val.split('\n')[0]
        target = val2[0]
        featureval = val2[1:].split(' ')
        dict1={}
        for val1 in featureval[1:]:
            list1 = val1.split(':')
            dict1[int(list1[0])]=float(list1[1])
        sorted_x = sorted(dict1.items(), key=operator.itemgetter(0))
        finalstr=''
        for val in sorted_x:
            finalstr+=' '+str(val[0])+':'+str(val[1])
        finalstr=str(target)+finalstr
        w.write(finalstr + '\n')
w.close()
