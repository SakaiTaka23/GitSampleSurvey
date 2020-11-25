import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv',index_col=0)

# print("平均")
# commit = data['Commit'].mean()
# print(commit)
# star = data['Star'].mean()
# print(star)
# pub_repo = data['Public_repo'].mean()
# print(pub_repo)

# print("中央値")
# commit = data['Commit'].median()
# print(commit)
# star = data['Star'].median()
# print(star)
# pub_repo = data['Public_repo'].median()
# print(pub_repo)

# print("標準偏差")
# commit = data['Commit'].std()
# print(commit)
# star = data['Star'].std()
# print(star)
# pub_repo = data['Public_repo'].std()
# print(pub_repo)



plt.figure()
data['Public_repo'].hist()
plt.savefig('result.jpg')
plt.close('all')