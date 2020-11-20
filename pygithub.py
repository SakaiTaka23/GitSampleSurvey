from repo_process import repo_process
from get_random_user import get_random_name
from github import Github

g = Github()

rand_name = get_random_name()
rand_name = "SakaiTaka23"
print(rand_name)

repo_count = 0
commit_count = 0
star_count = 0

for repo in g.get_user(rand_name).get_repos(type='public'):
    print("------------------------------")
    print(repo.full_name)
    counts = repo_process(repo.full_name)
    commit_count += counts[0]
    star_count += counts[1]
    repo_count = repo_count + 1
    print(commit_count,star_count,repo_count)
    print("------------------------------")


print("commit_count")
print(commit_count)
print("star_count:")
print(star_count)
print("repo_count")
print(repo_count)

# user = g.get_user()
# print(user.login)

# repo = g.get_repo("SakaiTaka23/node_app")
# print(repo.stargazers_count)

