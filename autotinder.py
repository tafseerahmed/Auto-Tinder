import requests
import json
import numpy as np
import tinder_api as ti
from recommendations import tinderlogin,recGen
from customvision_model import like_or_nope
import pandas as pd
from tindertool import mkdir
import os
import config
from PIL import Image
from io import BytesIO

AGE_MIN = 18
AGE_MAX = 24
DISTANCE = 100


def stats(likes, nopes):
    prop_likes = (float(likes) / (likes + nopes)) * 100.0
    prop_nopes = 100.0 - prop_likes
    print('likes = {} ({}%), nopes = {} ({}%)'.format(likes, prop_likes,
                                                      nopes, prop_nopes))

def saveLog(mark,url,id_):
    if os.path.isfile(f'./data/images/marked/{mark}-{id_}.jpg') == False:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.save(f'./data/images/marked/{mark}-{id_}.jpg')


if __name__ == "__main__":    
    like_ids,dislike_ids = [],[]
    tinderlogin(config.username,config.password)
    mkdir(f'./data/images/marked')
    ti.change_preferences(age_filter_min=AGE_MIN,age_filter_max=AGE_MAX,distance_filter=DISTANCE)
    rate_limited=0
    while True:
        rec = ti.get_recs_v2()["data"]["results"]
        for user in rec:
            id_ = user["user"]["_id"]
            if 'tinder_rate_limited_id' in str(user):
                print('Limit reached.')
                rate_limited=1
                break
            url = user["user"]['photos'][0]["processedFiles"][0]["url"]
            if like_or_nope(url) == 1:
                ti.like(id_)
                like_ids.append(id_)
            else:
                ti.dislike(id_)
                dislike_ids.append(id_)
        if rate_limited == 1:
                 break
    
    for i in like_ids:
        user = ti.get_person(i)["results"]
        id_ = user["_id"]
        url = user['photos'][0]["processedFiles"][0]["url"]
        saveLog("like",url,id_)   
    
    for id_ in dislike_ids:
        user = ti.get_person(i)["results"]
        id_ = user["_id"]
        url = user['photos'][0]["processedFiles"][0]["url"]
        saveLog("dislike",url,id_)  

    print(stats(len(like_ids),len(dislike_ids)))
    