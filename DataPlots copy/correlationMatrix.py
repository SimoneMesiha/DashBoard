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

# pd.to_numeric(data['Enrollment'])
#
#
# #print(data.columns[0])
# print(data['% ELL'])
print(data.corr())
data=data.corr()
data.to_csv('Correlation.csv')