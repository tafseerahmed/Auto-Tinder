import requests
import json
import numpy as np


pred_url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/a8c3b641-3ec2-41c5-85d4-db922d488dbb/url?iterationId=c3e9edd5-0748-4a30-a58f-b2b102d41bec"
headers = {
            'Prediction-Key': 'c070a93c50664a85b82c114278b4e4c1',
            'Content-Type': 'application/json'
            }

def like_or_nope(url):
    r = requests.post(pred_url, data = json.dumps({'Url':url}), headers=headers).json()
    if r['predictions'][0]['tagName']=='like':
       	print ("Like!")
       	return 1
    else:
        print("Dislike!")
        return 0
