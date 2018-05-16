import xml.etree.ElementTree as ET
import csv
import json
from decimal import Decimal

tree = ET.parse("map.xml")
root = tree.getroot()

# open a file for writing

# mapData = open('map_data.csv','w')



# create the csv writer object

# csvwriter = csv.writer(mapData)
# resident_head = []
# count = 0

nodes= root.findall('node')
print("length of nodes is ",len(nodes))
rootTag=root.findall('way')
noOfWays=len(rootTag)
print("total ways are",noOfWays)

# a=[ node for node in root.findall('way') if node.findtext('tag')]
waysArray=[]



wayDict={}

fileNames=[]

count=0
flag=0
countWay=0
countHighway=0
countName=0
index=0
for way in rootTag:
    # print("in for loop")
    tags=way.findall('tag')
    countWay=countWay+1
    # print(len(tags))
    for tag in tags:
     
        
        
        if tag.attrib['k']=='highway':
            countHighway=countHighway+1
            print("\n")
            print("\n")
            wayDict={}
            flag = flag+1
            wayDict['value']=tag.attrib['v']
            wayDict['id']=way.attrib['id']
            
            i=0
            while(i<len(fileNames)):
                if fileNames[i]==tag.attrib['v']+".json":
                    index=i
                    print("found index value is ",index)
                    break
                i=i+1
            
            if i==(len(fileNames)):
                v= tag.attrib['v']+".json"
                print("v is ",v)
                fileNames.append(v)
                print(" not found file appended ",fileNames)
                index=i
                print("not found index value is ",index)

            print("file name array is ",fileNames)


            for subTag in tags:
                if subTag.attrib['k']=='name':
                    countName = countName + 1
                    wayDict['name']=subTag.attrib['v']

            



            # print("dfgfdkg")
            # count=count+1
            # wayDict['value']=tag.attrib['value']
            # wayDict['id']=way.attrib['id']
            nds= way.findall('nd')
            print("Total nds are :",len(nds))
            count=0
            nodesKeyArray=[]
            for nd in nds:
                # print("ref ",nd.attrib)
                for node in nodes:
                    # count=count+1
                    
                    if nd.attrib['ref']==node.attrib['id']:
                        count=count+1
                        # print("hey")
                        latLong={}
                        # print(node.attrib['lat'])
                        # print(node.attrib['lon'])
                        latLong['lat']=float(node.attrib['lat'])
                        latLong['lng']=float(node.attrib['lon'])
                        # print(latLong)
                        nodesKeyArray.append(latLong)
                        # print()
                        break
                

            wayDict['nodesKey']=nodesKeyArray
            wayDict['count']=count

            # print json.dumps(wayDict, ensure_ascii=False,indent=4)
            waysArray.append(wayDict)
            
            with open('data/'+fileNames[index], 'a+') as outfile: 
                print("file name is ",fileNames[index])
                json.dump(wayDict, outfile,ensure_ascii=False,indent=4)
            print(count)
            break
    # print("\n")
    print("\n")
    print("No of Highways:",countHighway)              
    print("Count of ways :",countWay)              
    print("Named Highways:",countName)
    print("Progress      : ",round((float(countWay)/float(noOfWays))*100.0,2)," percent")              
        
    
    # if flag==22:
    #     break
            
                        
print(len(waysArray)," waysArray")

    # break
# print(count+1)

# for member in root.findall('tag'):
	# if rootTag.get('k') == 'highway':
    # 		print("hey")
# print(root.getchildren()[100])

# dir(root)
# 	resident = []
# 	address_list = []
# 	if count == 0:
# 		name = member.find('latitude').tag
# 		resident_head.append(name)
# 		PhoneNumber = member.find('longitude').tag
# 		resident_head.append(PhoneNumber)
# 		EmailAddress = member.find('EmailAddress').tag
# 		resident_head.append(EmailAddress)
# 		Address = member[3].tag
# 		resident_head.append(Address)
# 		csvwriter.writerow(resident_head)
# 		count = count + 1

# 	name = member.find('Name').text
# 	resident.append(name)
# 	PhoneNumber = member.find('PhoneNumber').text
# 	resident.append(PhoneNumber)
# 	EmailAddress = member.find('EmailAddress').text
# 	resident.append(EmailAddress)
# 	Address = member[3][0].text
# 	address_list.append(Address)
# 	City = member[3][1].text
# 	address_list.append(City)
# 	StateCode = member[3][2].text
# 	address_list.append(StateCode)
# 	PostalCode = member[3][3].text
# 	address_list.append(PostalCode)
# 	resident.append(address_list)
# 	csvwriter.writerow(resident)


# mapData.close()
