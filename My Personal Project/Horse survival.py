import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglometrativeClustering
from sklearn.metrics import pairwise_distances

data = pd.read_csv('zoo.csv')

import numpy as np
labels = data['class_type']


features = data.values[:,1:-1]


model = AgglometrativeClustering(n_clusters=7,linkage='average',affinity='cosine')
model.fit(features)
