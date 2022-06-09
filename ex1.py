import json

data = json.load(open('C:\\Users\\matth\\Downloads\\exercises-main\\exercise-01\\data\\devices.json', encoding='utf-8'))
devices = []

def getUUID(info):
    uuid = ""

    if "uuid:" in info:
        temp = info.split(',')
        #The uuid is 36 characters long, so we take the last 36 characters
        uuid = temp[0][-36:]
    else:
        uuid = "ERROR - No UUID found"

    return uuid
def sortByName(e):
    return e['Name'].upper()

def reformatData(data):
    devices = []
    #Loop through the devices in our data
    for device in data['Devices']:
        payloadTotal = 0
        uuid="-1"

        uuid = getUUID(device["Info"])

        #Loop through the sensors in the device, get the total payload
        for sensor in device["Sensors"]:
            payloadTotal = payloadTotal + sensor["Payload"]
    
    #python dict that will be added to the array of devices
        dev = {
            "Name":device["Name"],
            "Type":device["Type"],
            "Info":device["Info"],
            "Uuid":uuid,
            "PayloadTotal":payloadTotal
            }
        devices.append(dev)

    return devices

devices = reformatData(data)
devices.sort(key=sortByName)
for i in devices:
    print(i , '\n')

x = json.dumps(devices)

try:
    outFile = open("C:\\Users\\matth\\Downloads\\exercises-main\\outFile.json" , "x")
except:
    outFile = open("C:\\Users\\matth\\Downloads\\exercises-main\\outFile.json" , "w")

outFile.write(x)
outFile.close()
