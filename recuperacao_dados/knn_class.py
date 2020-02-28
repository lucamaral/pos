from scipy.stats import mode

class Knn:

    # construtor
    def __init__(self,k):
        self._k = k

    def fit(self, X_train, y_train):
        self._X_train = X_train # Train
        self._y_train = y_train # Train

    def predict(self, X_test):
        results = []
        for i in range(len(X_test)):
            X_test_row = X_test[i, :]

            # distancia euclidiana
            diferenca_quadrado = (self._X_train - X_test_row) ** 2
            distancia = diferenca_quadrado.sum(axis=1)

            # ordena da menor para a maior distância e pega as primeiras "k" distâncias
            min_k = distancia.argsort()[:self._k]
            # pega o valor mais frequente (moda)
            label = mode(self._y_train[min_k]).mode[0]
            results.append(label)
        return results
    
