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
print(public_repos,followers)


url = 'https://api.github.com/search/issues?q=+type:pr+user:'+ name +'&sort=created&order=asc'
r = requests.get(url)
data = json.loads(r.text)

pull_requests = data['total_count']
print(pull_requests)

g = Github(token)
issues = g.get_user().get_user_issues()
print(issues.totalCount)
