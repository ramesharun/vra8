import winrm

#Global Variables
event              = ""                                          #Provision or remove.
hostname           = ""                                          #Cleaned up Hostname
domain_controller  = "dc.cmplab.dk"                              #Domain controller FQDN
OU                 = "OU=VRA,DC=cmplab,DC=dk"              #OU Where to place the computer in format CN=xxx,DC=xxx,DC=xxx
Username           = "administrator"                             #Username with right to do the operation
Password           = "VMware9!"                                  #Password for the account" 
Project            = ""                                          #Projct Name

#Get inputs from deployment
def get_vm_input(context, inputs):
    global event
    global hostname
    global Project
    global OU
        
    event         = str(inputs["__metadata"]["eventTopicId"])   #Provision or remove - Not used yet. 
    hostname_raw  = inputs["resourceNames"]                     #Raw Hostname
    hostname      = str(hostname_raw)[2:-2]                     #Cleaned up Hostname
    Project       = str(inputs["customProperties"]["projectname"]) #Project Name
    OU = "OU="+Project+","+OU                                   #Update OU to match Project
    
    
def handler(context, inputs):
    get_vm_input(context, inputs)
    #Open session
    session = winrm.Session(domain_controller, auth=(Username,Password))
    
    #Check for provision
    result = event.startswith('compute.provision')
    if result == True :
      dns_command = "dsadd computer cn="+hostname+","+OU+""
      result = session.run_ps(dns_command)
      print(result.std_out)

    #Check for removal
    result = event.startswith('compute.removal')
    if result == True :
      dns_command = "dsrm cn="+hostname+","+OU+" -noprompt"
      result = session.run_ps(dns_command)
      print(result.std_out)
