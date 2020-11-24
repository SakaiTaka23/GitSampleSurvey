import pandas
from pandas import plotting

data = pandas.read_csv('result.csv',sep=';', na_values=".")
print(data)
