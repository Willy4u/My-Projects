from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


X,y =load_digits(n_class=2,return_X_y=True)

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=2)
mlp = MLPClassifier()
mlp.fit(X_train,y_train)

x=X_test[3]
plt.matshow(x.reshape(8,8),cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
plt.show()
print(mlp.predict([x]))
print(mlp.score(X_test,y_test))
