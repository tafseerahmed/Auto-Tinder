
import json
import tinder_api as ti
from customvision_model import like_or_nope
import fb_auth_token as fb
import config

AGE_MIN = 18
AGE_MAX = 24
DISTANCE = 100

def tinderlogin(usrname,password):
    fb_access_token = fb.get_fb_access_token(usrname, password)
    fb_user_id = fb.get_fb_id(fb_access_token)
    token = ti.get_auth_token(fb_access_token, fb_user_id)
    if token:
        return False
    return True

def stats(likes, nopes):
    prop_likes = (float(likes) / (likes + nopes)) * 100.0
    prop_nopes = 100.0 - prop_likes
    print('likes = {} ({}%), nopes = {} ({}%)'.format(likes, prop_likes,
                                                      nopes, prop_nopes))

if __name__ == "__main__":    
    like_ids,dislike_ids = [],[]
    tinderlogin(config.username,config.password)
    ti.change_preferences(age_filter_min=AGE_MIN,age_filter_max=AGE_MAX,distance_filter=DISTANCE)
    rate_limited=0
    while True:
        rec = ti.get_recs_v2()["data"]["results"]
        for user in rec:
            id_ = user["user"]["_id"]
            url = user["user"]['photos'][0]["processedFiles"][0]["url"]
            try:
                if like_or_nope(url) == 1:
                    ti.like(id_)
                    like_ids.append(id_)
                else:
                    ti.dislike(id_)
                    dislike_ids.append(id_)
            except:
                rate_limited=1
        if rate_limited==1:
            print('Limit reached.')
            break
    print(stats(len(like_ids),len(dislike_ids)))
    