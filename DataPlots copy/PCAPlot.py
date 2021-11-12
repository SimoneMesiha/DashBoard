import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

data = pd.read_csv('8Col.csv')
scaled_data = preprocessing.scale(data.T)  # preProcess data

# print(scaled_data)
pca = PCA()
pca.fit(scaled_data)
pca_data = pca.transform(scaled_data)
# print(pca_data)
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
print(per_var)

plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
#plt.show()
