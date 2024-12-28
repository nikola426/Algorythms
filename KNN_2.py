"""
Алгоритм k-ближайших соседей (KNN) — это простой и эффективный метод классификации и регрессии, основанный на принципе
"ближайших соседей". Он работает, находя kk ближайших точек в обучающем наборе данных и делая прогноз на основе их меток.
Если вы хотите использовать уже готовую реализацию KNN из библиотеки scikit-learn, это можно сделать следующим образом:
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Примерные данные: 4 точки с 2 признаками и метками классов
X = np.array([[1, 2], [2, 3], [3, 1], [6, 5]])
y = np.array([0, 0, 0, 1])  # Метки классов

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Создание и обучение модели KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Предсказание на тестовых данных
predictions = knn.predict(X_test)

print("Предсказанные метки:", predictions)
