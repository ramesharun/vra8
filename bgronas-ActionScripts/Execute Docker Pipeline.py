import json

def handler(context, inputs):
    payload = {}
    
    pl = json.dumps(payload)
    
    url = "/codestream/api/pipelines/f96cb64f2ee2d47558754719881c2/executions"
   
    r = context.request(url, 'POST', pl)
    


