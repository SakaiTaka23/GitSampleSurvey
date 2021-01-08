from dotenv import load_dotenv
import os
from github import Github
import requests
import json

load_dotenv()
token = os.environ['api_token']

url = 'https://api.github.com/users/'
name = 'SakaiTaka23'

url = url + name
r = requests.get(url)
data = json.loads(r.text)

public_repos = data['public_repos']
followers = data['followers']
print("public_repo: "+str(public_repos))
print("followers: "+str(followers))


url = 'https://api.github.com/search/issues?q=+type:pr+user:' + \
    name + '&sort=created&order=asc'
r = requests.get(url)
data = json.loads(r.text)

pull_requests = data['total_count']
print("pull_requests: "+str(pull_requests))

g = Github(token)
issues = g.get_user().get_user_issues()
print("issues: "+str(issues.totalCount))


def repo_process(full_repo_name, g):
    repo = g.get_repo(full_repo_name)
    # print(dir(repo))
    total_star = repo.stargazers_count
    try:
        total_commit = repo.get_commits().totalCount
    except Exception:
        # リポジトリが空の時に発生
        total_commit = 0
    return total_commit, total_star


commit_sum = 0
star_sum = 0
for repo in g.get_user(name).get_repos(type='public'):
    if repo.fork:
        continue
    counts = repo_process(repo.full_name, g)
    commit_sum += counts[0]
    star_sum += counts[1]

print("commit_sum: "+str(commit_sum))
print("star_sum: "+str(star_sum))
