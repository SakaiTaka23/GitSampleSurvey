from github import Github

# First create a Github instance:

# using username and password
# g = Github("user", "password")

# or using an access token
g = Github()

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:

for repo in g.get_user("SakaiTaka23").get_repos(type='public'):
    print(repo.name)

# user = g.get_user()
# print(user.login)

# repo = g.get_repo("SakaiTaka23/node_app")
# print(repo.stargazers_count)

