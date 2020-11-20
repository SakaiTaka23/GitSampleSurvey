from get_random_user import get_random_name
from github import Github

# First create a Github instance:

# using username and password
# g = Github("user", "password")

# or using an access token
g = Github("70efe5d72622d2531729b46982470622ef6ec03a")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:

rand_name = get_random_name()
print(rand_name)
for repo in g.get_user(rand_name).get_repos(type='public'):
    print(repo.name)

# user = g.get_user()
# print(user.login)

# repo = g.get_repo("SakaiTaka23/node_app")
# print(repo.stargazers_count)

