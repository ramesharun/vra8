import requests
 
def handler(context, inputs):
    # Modify the URL to point to your Gitlab, Github or any other URL that holds the ssh key
    response = requests.get('https://github.com/rhjensen79.keys')
    # Set encodding to UTF-8
    response.encoding = 'utf-8'
    # Remove new line breaks from the text
    ssh_key = response.text.replace("\n","")
    print(ssh_key)
 
    # Read the sshKey value from the Properties section fo the blueprint payload
    old_key = inputs["customProperties"]["sshKey"]
    new_key = ssh_key
    
    # Create outputs and assing new key valye
    outputs = {}
    outputs["customProperties"] = inputs["customProperties"]
    outputs["customProperties"]["sshKey"] = new_key
 
    print("Setting machine sshKey value from {0} to {1}".format(old_key, new_key))
 
    return outputs