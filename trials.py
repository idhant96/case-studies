import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_excel('data/DOCTOR_THERAPY_PREFERENCES.xlsx')
X = df.iloc[:, [3,5,6,7]].values

inerts = []

for i in range(1, 20, 1):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    inerts.append(kmeans.inertia_)

plt.plot(range(1, 20), inerts)
plt.title('cluster bolo')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()







