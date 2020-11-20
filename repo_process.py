from github import Github

def repo_process(full_repo_name):
    g = Github()
    repo = g.get_repo(full_repo_name)
    total_star = repo.stargazers_count
    total_commit = repo.get_commits().totalCount
    return total_commit,total_star
    
