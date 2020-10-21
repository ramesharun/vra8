import json
import boto3
from   datetime import datetime

#Global Variables
event          = ""                                          #Provision or remove.
ipadress       = ""                                          #Cleaned up IP
hostname       = ""                                          #Cleaned up Hostname
description    = "App description etc. "                     #Application Description - Used for Project name
owner          = ""                                          #The requester of the ressource
revenue_impact = "0"                                         #Revenue impacted 
projectname    = "Unknown"                                   #The project the deployment belongs to
timesaved      = '30'                                        #Default time saved

#Get inputs from deployment
def get_vm_input(context, inputs):
    global event
    global ipadress
    global hostname
    global requestid
    global owner
    global projectname
    global timesaved
        
    event         = str(inputs["__metadata"]["eventTopicId"])          #Provision or remove - Not used yet. 
    ip_raw        = inputs["addresses"]                                #Raw IP input
    ipadress      = str(ip_raw[0])[2:-2]                               #Cleaned up IP
    hostname_raw  = inputs["resourceNames"]                            #Raw Hostname
    hostname      = str(hostname_raw)[2:-2]                            #Cleaned up Hostname
    owner         = str(inputs["__metadata"]["userName"])              #The requester of the ressource
    if 'projectname' in inputs["customProperties"]:
      projectname   = str(inputs["customProperties"]["projectname"])
    else:
      inputs["customProperties"]["projectname"] = projectname
    if 'timesaved' in inputs["customProperties"]:
      timesaved   = str(inputs["customProperties"]["timesaved"])
    else:
      inputs["customProperties"]["timesaved"] = timesaved
    return inputs
    

def write_db():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CMPvalue')

    table.put_item(
    Item={
        'datetime': datetime.utcnow().isoformat(),
        'hostname': hostname,
        'type': 'vm',
        'timesaved': timesaved,
        'requester': owner,
        'revenue_impact': revenue_impact,
        'projectname' : projectname

    }
    )

def handler(context, inputs):
    get_vm_input(context, inputs)
    write_db()


