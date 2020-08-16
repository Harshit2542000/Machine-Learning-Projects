# -*- coding: utf-8 -*-
"""Copy of hierarchical_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14I-eogOBvL-iaiYPZv39Ma2wG7j2jEa-

# Hierarchical Clustering

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset=pd.read_csv("Mall_Customers.csv")
X=dataset.iloc[ : ,[3,4]].values

"""## Using the dendrogram to find the optimal number of clusters"""

import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(X,method="ward"))
plt.title("dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distances")
plt.show()

"""## Training the Hierarchical Clustering model on the dataset"""

from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity="euclidean",linkage="ward")
y_hc=hc.fit_predict(X)

print(y_hc)

"""## Visualising the clusters"""

plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=100,c="red",label="Cluster 1")
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=100,c="blue",label="Cluster 2")
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=100,c="green",label="Cluster 3")
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=100,c="cyan",label="Cluster 4")
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=100,c="magenta",label="Cluster 5")
plt.title("Cluster of Customers")
plt.legend()
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")