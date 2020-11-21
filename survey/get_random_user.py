import random
import requests


def get_random_name():
    rand_id = random.randint(1,70000000)
    url = "https://api.github.com/user/"
    api = requests.get(url+str(rand_id)).json()
    name = api['login'].replace("'","")
    return name
