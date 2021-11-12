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

order = ['Num of SAT Test Takers', 'Enrollment', '% Black or Hispanic', 'SAT Critical Reading Avg. Score',
         'SAT Math Avg. Score', '% Overage', '% ELL', '% Students with Disabilities']

data = data.reindex(columns=order)
data.to_csv('sortedCols.csv')

