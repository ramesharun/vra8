import json


def handler(context, inputs):

    deploymentid = str(inputs["deploymentId"])
    
    print ("Deploymentid : "+deploymentid)
    
    
    payload = {}
    
    pl = json.dumps(payload)
    
    url = "/deployment/api/deployments/"+deploymentid+""
    r = context.request(url, 'DELETE', pl)
    print(r['content'])
    

