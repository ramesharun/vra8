#Variables
outputs = {}

def githubuser(context, inputs):
    #Define Users
    users = {
        "jensenr@vmware.com": "rhjensen79",
        "reilersen@vmware.com": "rasmusraskeilersen",
        "ktholstorf@vmware.com": "KimTholstorf",
        "robert@robert-jensen.dk": "rhjensen79",
        "jthomsen@vmware.com": "rhjensen79"
    }
    
    #Get input
    requester = str(inputs["__metadata"]["userName"]) 
    print ("Requester is : ",requester)
    
    #Copy Input to output
    global outputs
    outputs["customProperties"] = inputs["customProperties"]
    
    #Set new value based on requester
    outputs["customProperties"]["github"] = users[requester]
    print ("Github Username is : " + users[requester])

    return outputs
    
def handler(context, inputs):
    global outputs
    
    githubuser(context, inputs)
    
    return outputs