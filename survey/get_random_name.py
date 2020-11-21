import random
import requests

def get_random_name(api_token):
    rand_id = random.randint(1,70000000)
    url = "https://api.github.com/user/"
    api = requests.get(url+str(rand_id)+"?access_token="+api_token).json()
    name = api['login'].replace("'","")
    return name
