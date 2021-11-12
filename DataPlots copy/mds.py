from sklearn.manifold import MDS
from matplotlib import pyplot as plt
import sklearn.datasets as dt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import manhattan_distances, euclidean_distances
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


correlationMatrix = [
    [1-1.0, 1-0.44, 1-0.53, 1-0.95, 1-0.25, 1-0.28, 1-0.55, 1-0.09],
    [1-0.44, 1-1.0, 1-0.93, 1-0.32, 1-0.41, 1-0.68, 1-0.68, 1-0.49],
    [1-0.53, 1-0.93, 1-1.0, 1-0.42, 1-0.51, 1-0.60, 1-0.80, 1-0.31],
    [1-0.95, 1-0.32, 1-0.42, 1-1.0, 1-0.18, 1-0.20, 1-0.48, 1-0.05],
    [1-0.25, 1-0.41, 1-0.51, 1-0.18, 1-1.0, 1-0.18, 1-0.48, 1-0.31],
    [1-0.28, 1-0.68, 1-0.60, 1-0.20, 1-0.18, 1-1.0, 1-0.40, 1-0.68],
    [1-0.55, 1-0.68, 1-0.80, 1-0.48,1- 0.48, 1-0.40, 1-1.0, 1-0.04],
    [1-0.09, 1-0.49, 1-0.31, 1-0.053, 1-0.31, 1-0.68, 1-0.04, 1-1.0]
]


X = pd.read_csv('8Col.csv')
Y= correlationMatrix
mds = MDS(random_state=0)
X= mds.fit_transform(X)
Y=mds.fit_transform(Y)
print(X)
# np.savetxt("mds.csv",X,delimiter=",")
np.savetxt("mds2.csv",Y,delimiter=",")