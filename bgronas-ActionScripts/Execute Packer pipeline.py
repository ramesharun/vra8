import json

def handler(context, inputs):
    payload = {}
    
    pl = json.dumps(payload)
    
    #url = "/pipeline/api/pipelines/99fa396e2ca6f475584db9886beaa/executions"
    #url = "/codestream/api/pipelines/99fa396e2ca6f475584db9886beaa/executions"
    url = "/codestream/api/pipelines/d71f445a-89d0-46f1-a823-c54b3ffd80c5/executions"
    r = context.request(url, 'POST', pl)
    print(r['content'])
    


