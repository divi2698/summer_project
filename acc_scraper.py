# from datetime import datetime
# import time
import numpy as np
import json
import math as m

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)



file = open("u/DATA_08_07_23/All/Bus_ACC_2018_02_15_08_07_28_106.txt", "r")
line1 = file.read().splitlines()
    # print(lines)


# lines1=[x.strip('\n') for x in lines]

# lines=line1[1].split(',')
lines=[]
for line in line1:
    lines.append(line.split(','))
# print(lines)


firstTimeSample=0

t=0
print("length of the lines list is : ",len(lines))

i=1

xAccArray=[]
yAccArray=[]
zAccArray=[]
rAccArray=[]
xAcc=[]
yAcc=[]
zAcc=[]
rAcc=[]
timeArray=[]
dateArray=[]
while(i<len(lines)):
    
    l=lines[i]
    dateTime=l[3]
    # print(dateTime)
    dateTime=dateTime.split(' ')
    date=dateTime[0]
    time=dateTime[1]
    
    timeSeconds=get_sec(time)

    if i==1:
        firstTimeSample=timeSeconds
    
    # print(timeSeconds)

    # print("first time sample is ",firstTimeSample)
    # print("\n")


    t=timeSeconds-firstTimeSample

    if i!=1:
        if prevTime==t:
            xAcc.append(l[0])
            yAcc.append(l[1])
            zAcc.append(l[2])
            rAcc.append(m.sqrt(float(l[0])*float(l[0])+float(l[1])*float(l[1])+float(l[2])*float(l[2])))
        elif t==prevTime+1:
            x=[]
            y=[]
            z=[]
            r=[]

            for j in xAcc:
                x.append(float(j))
            for j in yAcc:
                y.append(float(j))
            for j in zAcc:
                z.append(float(j))
            for j in rAcc:
                r.append(j)
            # print("r is ",r)
            

            # print("x is ",x)

            xAccArray.append(x)
            yAccArray.append(y)
            zAccArray.append(z)
            rAccArray.append(r)

            # if i<85:
            #     print("xacc arr ", xAccArray)
            #     print("\n")
            xAcc.clear()
            yAcc.clear()
            zAcc.clear()
            rAcc.clear()

            # print("xacc is ",xAcc)

            xAcc.append(l[0])
            yAcc.append(l[1])
            zAcc.append(l[2])
            rAcc.append(m.sqrt(float(l[0])*float(l[0])+float(l[1])*float(l[1])+float(l[2])*float(l[2])))
            
            dateArray.append(prevDate)
            timeArray.append(prevTimeInFormat)
    else:
            xAcc.append(l[0])
            yAcc.append(l[1])
            zAcc.append(l[2])
            rAcc.append(m.sqrt(float(l[0])*float(l[0])+float(l[1])*float(l[1])+float(l[2])*float(l[2])))
        

    prevTime=t
    prevDate=date
    prevTimeInFormat=time
    # print("time is ",t)
    

    i=i+1

p=[]
q=[]
r=[]
s=[]
for j in xAcc:
    p.append(float(j))
for j in yAcc:
    q.append(float(j))
for j in zAcc:
    r.append(float(j))
for j in rAcc:
    s.append(j)

# for the last line
xAccArray.append(p)
yAccArray.append(q)
zAccArray.append(r)
rAccArray.append(s)

timeArray.append(prevTimeInFormat)
dateArray.append(prevDate)


# x3=x[3]
# x3=x3.split(' ')
# print (x3[1])
# print(xAcc)
xAccMean=[]
yAccMean=[]
zAccMean=[]
rAccMean=[]

xAccStd=[]
yAccStd=[]
zAccStd=[]
rAccStd=[]

# print("xAcc Array is ",xAccArray)
# print("xAcc Array is ",len(xAccArray))
# print("\n")
# print("yAcc Array is ",yAccArray)
# print("yAcc Array is ",len(yAccArray))
# print("\n")
# print("zAcc Array is ",zAccArray)
# print("zAcc Array is ",len(zAccArray))
# print("\n")
# print("rAcc Array is ",rAccArray)
# print("rAcc Array is ",len(rAccArray))
# print (get_sec(x3[1]))
c=0

for a1 in xAccArray:
    xAccMean.append(np.mean(a1))

for a1 in yAccArray:
    yAccMean.append(np.mean(a1))

for a1 in zAccArray:
    zAccMean.append(np.mean(a1))

for a1 in rAccArray:
    rAccMean.append(np.mean(a1))

# print('========================================================================')
# print("the mean of all the x acc is ",xAccMean)
# print("the mean of all the x acc is ",len(xAccMean))
# print("the mean of all the y acc is ",yAccMean)
# print("the mean of all the y acc is ",len(yAccMean))
# print("the mean of all the z acc is ",zAccMean)
# print("the mean of all the z acc is ",len(zAccMean))
# print("the mean of all the r acc is ",rAccMean)
# print("the mean of all the r acc is ",len(rAccMean))

    # if c==0:
    #     print("mean is ",np.mean(x))
    # c=c+1

for a1 in xAccArray:
    xAccStd.append(np.std(a1))

for a1 in yAccArray:
    yAccStd.append(np.std(a1))

for a1 in zAccArray:
    zAccStd.append(np.std(a1))

for a1 in rAccArray:
    rAccStd.append(np.std(a1))
    
# print('========================================================================')
# print("the std of all the x acc is ",xAccStd)
# print("the std of all the x acc is ",len(xAccStd))
# print("the std of all the y acc is ",yAccStd)
# print("the std of all the y acc is ",len(yAccStd))
# print("the std of all the z acc is ",zAccStd)
# print("the std of all the z acc is ",len(zAccStd))
# print("the std of all the r acc is ",rAccStd)
print("the std of all the r acc is ",len(rAccStd))


with open('acc_statistical_data.json', 'a+') as fp:
    count=0
    fp.write('[')
    while(count<len(xAccMean)):
    
        obj={}
        xobj={}
        yobj={}
        zobj={}
        robj={}

        obj['seconds']=count
        obj["date"]=dateArray[count]
        obj["time"]=timeArray[count]

        xobj['mean']=xAccMean[count]
        xobj['standard deviation']=xAccStd[count]
        obj['x']=xobj
        
        yobj['mean']=yAccMean[count]
        yobj['standard deviation']=yAccStd[count]
        obj['y']=yobj

        zobj['mean']=zAccMean[count]
        zobj['standard deviation']=zAccStd[count]
        obj['z']=zobj
        
        robj['mean']=rAccMean[count]
        robj['standard deviation']=rAccStd[count]
        obj['resultant']=robj
        
        json.dump(obj, fp,ensure_ascii=False,indent=4)

        
        if count!=len(xAccMean)-1:
            fp.write(',')

        count=count+1
    fp.write(']')


# print("date array is ",dateArray)
print("date array is ",len(dateArray))
# print("time array is ",timeArray)
print("time array is ",len(timeArray))

file.close()

