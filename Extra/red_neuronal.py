from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_rn = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)

modelo_rn.fit(X_train, y_train)

predicciones_rn = modelo_rn.predict(X_test)
precision_rn = accuracy_score(y_test, predicciones_rn)

print("--- Algoritmo de Redes Neuronales ---")
print(f"Precisión de la Red Neuronal: {precision_rn * 100:.2f}%")