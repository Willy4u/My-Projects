import pandas as pd
import numpy as np

import matplotlib
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

import seaborn as sns
sns.set(style='white',color_codes=True)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn import metrics

df_train = pd.read_csv('train.csv')

df_train = df_train.drop(['PassengerId','Name','Cabin','Ticket'],axis=1)

def age_approx(cols):
    Age =cols[0]
    Pclass=cols[1]

    if pd.isnull(Age):
        if Pclass ==1:
            return 37
        elif Pclass ==2:
            return 29
        else:
            return 24
    else:
        return Age


df_train['Age']= df_train[['Age','Pclass']].apply(age_approx, axis=1)

df_train.dropna(inplace =True)


df_train_dummied = pd.get_dummies(df_train,columns=['Sex'])

df_train_dummied = pd.get_dummies(df_train_dummied,columns=['Embarked'])

plt.figure(figsize =(6,4))
sns.heatmap(df_train_dummied.corr())


used_features = ['Pclass','Age','SibSp','Parch','Sex_female','Sex_male','Embarked_C','Embarked_Q','Embarked_S']

X = df_train_dummied[used_features].values
y = df_train_dummied['Survived']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

LogReg = LogisticRegression()
LogReg.fit(X_train,y_train)

y_pred = LogReg.predict(X_test)
print(metrics.confusion_matrix(y_test,y_pred))
print(metrics.accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(LogReg.predict_proba(X_test))

