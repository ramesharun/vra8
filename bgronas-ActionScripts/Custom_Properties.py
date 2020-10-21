

def handler(context, inputs):
    token =  authenticate.authentificate(inputs["api_token"])
    project = get_project(token, inputs["projectId"])
    print (project)
    
    outputs = {}
    
    outputs["customProperties"] = inputs["customProperties"]
    outputs["customProperties"]["custom1234"] = "custom1234"

    
    return outputs


    

