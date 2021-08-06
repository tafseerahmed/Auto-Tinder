import requests
import json
import numpy as np


pred_url = "REMOVED"
headers = {
            'Prediction-Key': '##',
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
