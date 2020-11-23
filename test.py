from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
g = Github(os.environ['api_token'])
print(os.environ['api_token'])

rand_name = "SakaiTaka23"
print(rand_name)

for repo in g.get_user(rand_name).get_repos(type='public'):
    print("------------------------------")
    print(repo.full_name)
    print(repo.fork)
    print("------------------------------")
