import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('survey2/advanced-users.csv', index_col=0)

print("平均")
contributions = data['contributions'].mean()
pub_repos = data['pub repos'].mean()
stars = data['stars'].mean()
commits = data['commits'].mean()
pull_requests = data['pull requests'].mean()
issues = data['issues'].mean()
contribution = data['contribution'].mean()
followers = data['followers'].mean()
print(contributions)
print(pub_repos)
print(stars)
print(commits)
print(pull_requests)
print(issues)
print(contribution)
print(followers)

print("中央値")
contributions = data['contributions'].median()
pub_repos = data['pub repos'].median()
stars = data['stars'].median()
commits = data['commits'].median()
pull_requests = data['pull requests'].median()
issues = data['issues'].median()
contribution = data['contribution'].median()
followers = data['followers'].median()
print(contributions)
print(pub_repos)
print(stars)
print(commits)
print(pull_requests)
print(issues)
print(contribution)
print(followers)

print("標準偏差")
contributions = data['contributions'].std()
pub_repos = data['pub repos'].std()
stars = data['stars'].std()
commits = data['commits'].std()
pull_requests = data['pull requests'].std()
issues = data['issues'].std()
contribution = data['contribution'].std()
followers = data['followers'].std()
print(contributions)
print(pub_repos)
print(stars)
print(commits)
print(pull_requests)
print(issues)
print(contribution)
print(followers)
