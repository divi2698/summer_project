# import acc_scraper
import json

gpsFile = open("u/DATA_08_07_23/All/Bus_GPS_2018_02_15_08_07_28_106.txt", "r")
line1 = gpsFile.read().splitlines()

# print(line1)

lines=[]
for line in line1:
    lines.append(line.split(','))

# print(lines)

# array of objects of gps data containing lat long date and time
gpsDataArray=[]

i=1
while(i<len(lines)):
    obj={}
    l=lines[i]
    # print(l)
    obj["lat"]=float(l[0])
    obj["lng"]=float(l[1])
    dateTime=l[4]
    dateTime=dateTime.split(' ')
    obj["date"]=dateTime[0]
    obj["time"]=dateTime[1]
    gpsDataArray.append(obj)

    i=i+1


# print("gps data is : ",gpsDataArray)
# print("gps data array length is : ",len(gpsDataArray))


gpsFile.close()


wifiFile = open("u/DATA_08_07_23/All/Bus_WiFi_2018_02_15_08_07_28_186.txt", "r")
line1.clear()
line1 = wifiFile.read().splitlines()

# print("length of line1 is :",len(line1))
# print(line1)
lines.clear()
lines=[]
for line in line1:
    lines.append(line.split(','))

# print("length of lines is :",len(lines))

# array of objects of gps data containing lat long date and time
wifiDataArray=[]
macAddressArray=[]
signalStrengthArray=[]

i=0
while(i<len(lines)):
    obj={}
    l=lines[i]
    # print(l)
  
    dateTime=l[3]
    dateTime=dateTime.split(' ')
    date=dateTime[0]
    time=dateTime[1]

    if i!=0:
        if prevTimeInFormat==time:
            macAddressArray.append(l[0])
            signalStrengthArray.append(l[2])
        elif time!=prevTimeInFormat:
            x=[]
            y=[]
            for j in macAddressArray:
                x.append(j)
            for j in signalStrengthArray:
                y.append(int(j))

            obj={}
            obj["time"]=prevTimeInFormat
            obj["date"]=prevDate
            obj["mac addresses"]=x
            obj["signal strength"]=y
            wifiDataArray.append(obj)

            macAddressArray.clear()
            signalStrengthArray.clear()

            macAddressArray.append(l[0])
            signalStrengthArray.append(l[2])
    else:
        macAddressArray.append(l[0])
        signalStrengthArray.append(l[2])  
        

    prevDate=date
    prevTimeInFormat=time

    i=i+1


# for the last reading
p=[]
q=[]

for j in macAddressArray:
    p.append(j)
for j in signalStrengthArray:
    q.append(int(j))
sampleObj={}
sampleObj["time"]=prevTimeInFormat
sampleObj["date"]=prevDate
sampleObj["mac addresses"]=p
sampleObj["signal strength"]=q

wifiDataArray.append(sampleObj)

p.clear()
q.clear()



# print("wifi data is : ",wifiDataArray)
# print("wifi data array length is : ",len(wifiDataArray))

# with open('./samplewifi.txt','a+') as f:
#     for obj in wifiDataArray:
#         json.dump(obj, f,ensure_ascii=False,indent=4)


wifiFile.close()



