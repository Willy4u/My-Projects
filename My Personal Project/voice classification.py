import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('voice-classification.csv')
print(df.shape)
print('Total number of flabels:{}'.format(df.shape[0]))
print('Number of males:{}'.format(df[df.label=='male'].shape[0]))
print('Number of females:{}'.format(df[df.label=='female'].shape[0]))

from sklearn.preprocessing import LabelEncoder
y = df.iloc[:,-1]
gender_encoder = LabelEncoder()
y=gender_encoder.fit_transform(y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scler.transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=100)

from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix
