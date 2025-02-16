import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score,mean_squared_error
from math import sqrt



data = pd.read_csv('Advertising.csv',index_col=0)

data.columns =['TV','Radio','Newspaper','Sales']


fig,axes = plt.subplots(1,3,sharey=True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axes[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axes[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axes[2])


feature_cols=['TV']

x =data[feature_cols]
y= data.Sales
from sklearn.linear_model import LinearRegression

ln = LinearRegression()
ln.fit(x,y)

X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
preds = ln.predict(X_new)

data.plot(kind='scatter',x='TV',y='Sales')
plt.plot(X_new,preds,c='red',linewidth=2)
feature_cols = ['TV','Radio','Newspaper']
X= data[feature_cols]
y= data.Sales

from sklearn import model_selection
xtrain,xtest,ytrain,ytest = model_selection.train_test_split(X,y,test_size=0.3,random_state=42)
ln = LinearRegression()
ln.fit(X,y)
print(ln.intercept_)
print(ln.coef_)

ln = LinearRegression()
ln.fit(xtrain,ytrain)
print(ln.intercept_)
print(ln.coef_)

predictions = ln.predict(xtest)
print(sqrt(mean_squared_error(ytest,predictions)))
