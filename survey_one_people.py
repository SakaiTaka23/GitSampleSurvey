from repo_process import repo_process
from get_random_user import get_random_name
from github import Github
import os
from dotenv import load_dotenv
import random
import requests

def get_random_name(api_token):
    rand_id = random.randint(1,70000000)
    url = "https://api.github.com/user/"
    api = requests.get(url+str(rand_id)+"?access_token="+api_token).json()
    name = api['login'].replace("'","")
    return name

def repo_process(full_repo_name,g):
    repo = g.get_repo(full_repo_name)
    total_star = repo.stargazers_count
    total_commit = repo.get_commits().totalCount
    return total_commit,total_star

def survey_one_people(api_token):

    rand_name = get_random_name(api_token)
    # rand_name = "SakaiTaka23"
    print(rand_name)

    repo_sum = 0
    commit_sum = 0
    star_sum = 0
    g = Github(api_token)

    for repo in g.get_user(rand_name).get_repos(type='public'):
        print("------------------------------")
        print(repo.full_name)
        counts = repo_process(repo.full_name,g)
        commit_sum += counts[0]
        star_sum += counts[1]
        repo_sum += 1
        print(commit_sum,star_sum,repo_sum)
        print("------------------------------")


    print("user:")
    print(rand_name)
    print("commit_count:")
    print(commit_sum)
    print("star_count:")
    print(star_sum)
    print("repo_count")
    print(repo_sum)


load_dotenv()
api_token = os.environ['api_token']
survey_one_people(api_token)

