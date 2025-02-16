import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.datasets import load_boston
boston = load_boston()
boston.keys()
boston.feature_names
boston.target
print(boston.DESCR)
df = pd.DataFrame(boston.data)
df.shape
x_train = df.drop(['HOUSING_VALUE'], axis=1)
y_train = df['HOUSING_VALUE']
xtrain,xtest,ytrain,ytest = model_selection.train_test_split(x_train,y_train,test_size=0.3,random_state=42)
from sklearn.linear_model import LinearRegression
model = LinearRegression(n_jobs = -1)
model.fit(xtrain,ytrain)
print(model.intercept_)
print(model.coef_)
print(df.columns.values.tolist())
list(zip(df.columns,model.coef_))


