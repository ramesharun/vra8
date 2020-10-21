#Get project details from vRA
def get_projectDetails(context, projectId):
    print("Getting project from vRA for project ID: ", projectId)
    resp = context.request("/iaas/api/projects/"+projectId, "GET", "")
    json_resp = {}
    try:
        json_resp = json.loads(resp['content'])
    except json.decoder.JSONDecodeError as ex:
        print("Error occured while parsing json response: ")
        print(ex)
    print("Found Project: ", json_resp["name"])
    return json_resp
