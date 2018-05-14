import xml.etree.ElementTree as ET
import csv

tree = ET.parse("map.xml")
root = tree.getroot()

# open a file for writing

mapData = open('map_data.csv','w')

# create the csv writer object

csvwriter = csv.writer(mapData)
# resident_head = []
# count = 0

nodes= root.findall('node')
print("length of nodes is ",len(nodes))
rootTag=root.findall('way')
print("total ways are",len(rootTag))

# a=[ node for node in root.findall('way') if node.findtext('tag')]
waysArray=[]
wayDict={}
nodesKeyArray=[]
latLong={}


count=0
flag=0
for way in rootTag:
    # print("in for loop")
    tags=way.findall('tag')
    
    # print(len(tags))
    for tag in tags:
     
        if tag.attrib['k']=='highway':
            flag=1
            # print("dfgfdkg")
            # count=count+1
            # wayDict['value']=tag.attrib['value']
            # wayDict['id']=way.attrib['id']
            nds= way.findall('nd')
            print("total nds are",len(nds))
            count=0
            for nd in nds:
                print("ref ",nd.attrib)
                for node in nodes:
                    # count=count+1
                    
                    if nd.attrib['ref']==node.attrib['id']:
                        count=count+1
                        # print("hey")
                        print(node.attrib['lat'])
                        print(node.attrib['lon'])
                        latLong['lat']=node.attrib['lat']
                        latLong['lon']=node.attrib['lon']
                        # print(latLong)
                        nodesKeyArray.append(latLong)
                        # print()
                        break
        wayDict['nodesKey']=nodesKeyArray
        break              
    waysArray.append(wayDict)
    if flag==1:
        break         
                        
print(waysArray)

    # break
print(count)

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


mapData.close()
