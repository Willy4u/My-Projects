from sklearn.model_selection import GridSearchCV

from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
from IPython.display import Image
import numpy as np
import pandas as pd
from sklearn import tree
from matplotlib import pyplot as plt

df = pd.read_csv('titanic_dataset.csv')
df['male'] = df['Sex']=='male'

feature_names = ['Pclass','male','Age','Parch','SibSp']

X = df[feature_names].values
y = df['Survived'].values

model = DecisionTreeClassifier()




param_grid = {
'max_depth': [5,15,25],
'min_samples_leaf': [1,3],
'max_leaf_nodes' : [10,20,35,50]
}
gs = GridSearchCV(model,param_grid,scoring ='f1', cv=5)
gs.fit(X,y)
print(gs.best_params_)
