from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np
from scipy.stats import mode

(X, y) = load_iris(return_X_y=True)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=42)

K = 5

resultados = []

for X_test_row in X_test:
    distancias = []

    for X_train_row in X_train:
        diferenca_quadrado = (X_test_row - X_train_row) ** 2
        distancia = 0
        for dif_quad_item in diferenca_quadrado:
            distancia += dif_quad_item
        distancias.append(distancia)
    
    ordenado =    np.argsort(distancias)
    min_k = ordenado[:K]
    y_train_k_filtrados = y_train[min_k]
    moda = mode(y_train_k_filtrados)
    resultados.append(moda[0])

print('Score:', accuracy_score(y_test, resultados))