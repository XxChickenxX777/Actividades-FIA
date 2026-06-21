from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_knn = KNeighborsClassifier(n_neighbors=3)

modelo_knn.fit(X_train, y_train)

predicciones = modelo_knn.predict(X_test)
precision = accuracy_score(y_test, predicciones)

print("--- Algoritmo K-Nearest Neighbors ---")
print(f"Precisión del modelo: {precision * 100:.2f}%")