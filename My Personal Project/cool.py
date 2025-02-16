# Write your code here :-)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


cancer_data=load_breast_cancer()
df=pd.DataFrame(cancer_data['data'],columns=cancer_data['feature_names'])
df['target']=cancer_data['target']
X=df[cancer_data.feature_names]
y=cancer_data['target']

n_estimators=list(range(1,101))
params_grid={
    'n_estimators': n_estimators,
    }
rnd_state=123
rf=RandomForestClassifier(random_state=rnd_state)
gs=GridSearchCV(rf,params_grid,cv=5)
gs.fit(X,y)
 #collect max datapoints
max_scores=[]
scores=gs.cv_results_['mean_test_score'].round(4)
max_score=np.max(scores)
max_scores=[m for m in range(len(scores)) if scores[m] == max_score]

#Graph Info
title='Random state: '+ str(rnd_state)
plt.plot(n_estimators,scores)
plt.title(title,size=15)
plt.xlabel('n_estimators')
plt.ylabel('accuracy')
plt.xlim(0,100)
plt.ylim(0.9,1.0)
plt.plot([max_scores],[max_score],
        marker='o',
        markersize=10,
        markerfacecolor=None,
        markeredgecolor='r')
if len(max_scores) ==1 :
    max_text='max point ['+ str(max_scores[0])+','+str(max_score)+']'
    plt.annotate(s=max_text,xy=(max_scores[0],max_score),
                  xytext=(max_scores[0]-10,max_score+0.01),
                  color='r',
                  size=10)
else:
    max_text='max : '+str(max_score)+' ('+str(len(max_scores))+' points)'
