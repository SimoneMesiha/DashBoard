import pandas as pd
import seaborn
import matplotlib.pyplot as plt

data = pd.read_csv('cse332hw2 copy.csv')
# print(data)
# print(data.columns)

data.drop('DBN', inplace=True, axis=1)
data.drop('SCHOOL NAME', inplace=True, axis=1)
data.drop('Percentile Rank', inplace=True, axis=1)
data.drop('Environment Grade', inplace=True, axis=1)
data.drop('College and Career Readiness Grade', inplace=True, axis=1)
data.drop('% Students with Disabilities', inplace=True, axis=1)
data.drop('% Overage', inplace=True, axis=1)
data.drop('% ELL', inplace=True, axis=1)
print(data)
data.to_csv('5Col.csv')