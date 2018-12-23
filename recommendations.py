import tinder_api as ti
import fb_auth_token as fb
import json
import pandas as pd
import time
from datetime import date
import numpy as np
import os 


def tinderlogin(usrname,password):
    fb_access_token = fb.get_fb_access_token(usrname, password)
    fb_user_id = fb.get_fb_id(fb_access_token)
    token = ti.get_auth_token(fb_access_token, fb_user_id)
    if token:
        return False
    return True

def calculate_age(dob):
    today = date.today()
    dob_year = int(dob[:4])
    dob_month =int(dob[5:7])
    dob_day =int(dob[8:10])
    return today.year - dob_year - ((today.month, today.day) < (dob_month, dob_day))

def recGen(ageMin=18,ageMax=22,distance=100):
    ti.change_preferences(age_filter_min=ageMin,age_filter_max=ageMax,distance_filter=distance)
    recommendations = ti.get_recommendations()
    df =  pd.DataFrame.from_dict(recommendations["results"])
    df = df[['_id','name','gender','birth_date','bio','photos']]
    df = df.rename(index=str, columns={'_id':'ID','birth_date':'dob'})

    imgurls=[]
    for i in df['photos']:
        imgurls.append(i[0]['processedFiles'][0]['url'])

    df=df.drop(['photos'],axis=1)
    df['imgurl']=pd.Series(imgurls).values
    df["dob"] = df["dob"].apply(lambda x: calculate_age(x))
    df = df.rename(index=str, columns={"dob":"age"})
    return df
