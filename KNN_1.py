"""
Алгоритм k-ближайших соседей (KNN) — это простой и эффективный метод классификации и регрессии, основанный на принципе
"ближайших соседей". Он работает, находя kk ближайших точек в обучающем наборе данных и делая прогноз на основе их меток.
Ниже приведена реализация алгоритма KNN с использованием Python без сторонних библиотек.
"""


import numpy as np
import math


class KNN:
    def __init__(self, k=3):
        self.k = k  # Количество соседей

    def fit(self, X, y):
        """Обучает модель на данных X с метками y."""
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """Предсказывает метки для новых данных X."""
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        """Предсказывает метку для одной точки x."""
        # Вычисляем расстояния до всех точек в обучающем наборе
        distances = [self._euclidean_distance(x_train, x) for x_train in self.X_train]

        # Получаем индексы k ближайших соседей
        k_indices = np.argsort(distances)[:self.k]

        # Получаем метки ближайших соседей
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Возвращаем наиболее частую метку
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common

    def _euclidean_distance(self, point1, point2):
        """Вычисляет евклидово расстояние между двумя точками."""
        return math.sqrt(np.sum((point1 - point2) ** 2))


# Пример использования
if __name__ == "__main__":
    # Примерные данные: 4 точки с 2 признаками и метками классов
    X_train = np.array([[1, 2], [2, 3], [3, 1], [6, 5]])
    y_train = np.array([0, 0, 0, 1])  # Метки классов

    knn = KNN(k=3)
    knn.fit(X_train, y_train)

    # Новая точка для классификации
    X_test = np.array([[1.5, 2.5], [5, 5]])
    predictions = knn.predict(X_test)

    print("Предсказанные метки:", predictions)
