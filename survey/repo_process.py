def repo_process(full_repo_name,g):
    repo = g.get_repo(full_repo_name)
    # print(dir(repo))
    total_star = repo.stargazers_count
    try:
        total_commit = repo.get_commits().totalCount
    except Exception:
        # リポジトリが空の時に発生
        total_commit = 0
    return total_commit,total_star
