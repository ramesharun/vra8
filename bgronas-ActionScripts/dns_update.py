import winrm

#Global Variables
event         = ""                                          #Provision or remove.
ipadress      = ""                                          #Cleaned up IP
hostname      = ""                                          #Cleaned up Hostname
requestid     = ""                                          #Custom input value, containing Request id. Being  set in custom field later
project       = ""                                          #The project the deployment belongs to.
owner         = ""                                          #The requester of the ressource
DNS_Server    = "dc.cmplab.dk"                              #DNS server where the command will be executed
DNS_Domain    = "cmplab.dk"                                 #The DNS Domain to be updated
Username      = "administrator"                             #Username with right to do the operation
Password      = "VMware9!"                                  #Password for the account" 

#Get inputs from deployment
def get_vm_input(context, inputs):
    global event
    global ipadress
    global hostname
    global requestid
    global project
    global owner
        
    event         = str(inputs["__metadata"]["eventTopicId"])   #Provision or remove - Not used yet. 
    ip_raw        = inputs["addresses"]                         #Raw IP input
    ipadress      = str(ip_raw[0])[2:-2]                        #Cleaned up IP
    hostname_raw  = inputs["resourceNames"]                     #Raw Hostname
    hostname      = str(hostname_raw)[2:-2]                     #Cleaned up Hostname



def handler(context, inputs):
    get_vm_input(context, inputs)
    #Open session
    session = winrm.Session(DNS_Server, auth=(Username,Password))
    
    #Check for provision
    result = event.startswith('compute.provision')
    if result == True :
      dns_command = "dnscmd.exe "+DNS_Server+" /RecordAdd "+DNS_Domain+" "+hostname+" 10 A "+ipadress+""
      result = session.run_ps(dns_command)
      print(result.std_out)

    #Check for removal
    result = event.startswith('compute.removal')
    if result == True :
      dns_command = "dnscmd /RecordDelete "+DNS_Domain+" "+hostname+" a /f"
      result = session.run_ps(dns_command)
      print(result.std_out)

