from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from scipy.stats import mode

# para cada X_test
  # buscar distancias com X_train
  # pegar as K menores
  # criar novo array com K posicoes, buscando de y_train
  # pegar a moda desse novo array
  # armazenar em novo array de resultados   

(X, y) = load_iris(return_X_y=True)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=42)

K = 5

results = []

for i in range(len(X_test)):
    X_test_row = X_test[i, :]

    diferenca_quadrado = (X_train - X_test_row) ** 2
    distancia = diferenca_quadrado.sum(axis=1)

    # ordena da menor para a maior distância e pega as primeiras "k" distâncias
    min_k = distancia.argsort()[:K]
    # pega o valor mais frequente (moda)
    label = mode(y_train[min_k]).mode[0]
    results.append(label)

print('Score:', accuracy_score(y_test, results))