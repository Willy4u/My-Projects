import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize']=(12,6)

df = pd.read_csv('driver-data.csv')

from sklearn.cluster import KMeans

Kmeans = KMeans(n_clusters=2)
df_analyze = df.drop('id',axis=1)

Kmeans.fit(df_analyze)
print(Kmeans.cluster_centers_)

print(Kmeans.labels_)
print(len(Kmeans.labels_))
print(type(Kmeans.labels_))

unique,counts = np.unique(Kmeans.labels_,return_counts=True)
print(dict(zip(unique,counts)))

df_analyze['cluster'] = Kmeans.labels_

Kmeans_4 = KMeans(n_clusters= 4)
Kmeans_4.fit(df.drop('id',axis=1))
Kmeans_4.fit(df.drop('id', axis=1))
print(Kmeans_4.cluster_centers_)
unique,counts = np.unique(Kmeans_4.labels_,return_counts=True)
Kmeans_4.cluster_centers_

print(dict(zip(unique,counts)))

df_analyze['cluster']=Kmeans_4.labels_
sns.set_style('whitegrid')
sns.lmplot('mean_dist_day','mean_over_speed_prec',data =df_analyze,hue='cluster',palette='coolwarm',size=6,aspect=1,fit_reg=False)

