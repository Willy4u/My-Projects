from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.neural_network import MLPClassifier

X,y = fetch_openml('mnist_784',version=1,return_X_y=True)




mlp = MLPClassifier(hidden_layer_sizes=(6,),max_iter=200,alpha=1e-4,solver ='sgd',random_state=2)

mlp.fit(X,y)
print(mlp.coefs_[0].shape)
