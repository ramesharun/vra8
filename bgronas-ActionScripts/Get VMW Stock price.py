from urllib.request import urlopen
from contextlib import closing
from botocore.vendored import requests
import json
 
def lambda_handler():
    with closing(urlopen("https://financialmodelingprep.com/api/v3/stock/real-time-price/VMW")) as responseData:
        jsonData = responseData.read()
        deserialisedData = json.loads(jsonData)
        price = deserialisedData['price']
        print(price);
    return price

def handler(context, inputs):
    #Get webhook url from inputs
    webhook_url = "https://hooks.slack.com/services/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"
    
    #Build the message
    text = "VMW Stock is : " + price
    
    slack_data = {'text': text}
    
    #Post message
    response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
    )
    
price = str(lambda_handler())
