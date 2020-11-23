from survey.get_random_name import get_random_name
from survey.repo_process import repo_process
from github import Github

def survey_one_people(api_token):

    rand_name = get_random_name(api_token)
    #rand_name = "SakaiTaka23"
    print(rand_name)

    repo_sum = 0
    commit_sum = 0
    star_sum = 0
    g = Github(api_token)

    for repo in g.get_user(rand_name).get_repos(type='public'):
        print("------------------------------")
        print(repo.full_name)
        if repo.fork:
            print("is a forked repo")
            continue
        counts = repo_process(repo.full_name,g)
        commit_sum += counts[0]
        star_sum += counts[1]
        repo_sum += 1
        print(counts[0],counts[1])
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

    return rand_name,commit_sum,star_sum,repo_sum
