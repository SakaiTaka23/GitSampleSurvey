import random
import requests
import sys

def get_random_name(api_token):
    try_count = 1
    api = ""
    while try_count <= 3:
        rand_id = make_random_id()
        url = "https://api.github.com/user/"+str(rand_id)+"?access_token="+api_token
        api = requests.get(url)
        if api.status_code == requests.codes.ok:
            api = api.json()
            break
        elif try_count == 3:
            print("[Error] tried 3 times but failed...")
            sys.exit()
        else:
            try_count += 1
    name = api['login'].replace("'","")
    return name

def make_random_id():
    rand_id = random.randint(1,70000000)
    return rand_id
