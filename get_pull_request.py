from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
g = Github(os.environ['api_token'])

rand_name = "SakaiTaka23"
print(rand_name)

issues = g.search_issues('', author=rand_name, type='pr')
print(issues.totalCount)
