#PHPipam Cleanup script - Api documentation : https://phpipam.net/api/api_documentation/

import requests
import json

#Global Variables
phpipamhost   = "denmark-001243.cmplab.dk"                  #PHPIpam Host
app           = "VRA"                                       #PHPmyipam API App Name
app_token     = "mrtwifqVq250DENhrVpARzp0p7ej4cXV"          #PHPmyipam API App Token
token         = ""
Authorization = "Basic YWRtaW46Vk13YXJlOSE="

#Get token
def get_token():
    global token   
    url = "http://"+phpipamhost+"/api/"+app+"/user"
    payload  = {}
    headers = {
      'Content-Type': 'application/json',
      'token': ''+app_token+'',
      'Authorization': ''+Authorization+'',
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    #Get response as json
    data = response.json()
    #Set token Variable
    token = (data['data']['token'])
  
#Cleanup
def cleanup():
    #Get all Registered ID's
    url = "http://"+phpipamhost+"/api/"+app+"/addresses/"
    payload = "{}"
    headers = {
     'Content-Type': 'application/json',
     'token': ''+token+'',
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    
    #Convert response to json
    json_data = json.loads(response.text)

    #Run thru each item in data
    items = ""
    for item in json_data["data"]:
      id = (item['id'])
      #Check id status
      url = "http://"+phpipamhost+"/api/"+app+"/addresses/"+id+"/ping"
      response = requests.request("GET", url, headers=headers, data = payload)
      #Convert response to json
      result_data = json.loads(response.text)
      result = str(result_data['data']['result_code'])
      if result == "OFFLINE" :
        print (id +" Is offline - Deleting")
        url = "http://"+phpipamhost+"/api/"+app+"/addresses/"+id+""
        response = requests.request("DELETE", url, headers=headers, data = payload)
      else:
        print (id+" Is online - Skipping")

#Run Cleanup
def handler(context, inputs):
    get_token()
    cleanup()
   # return outputs
