from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_nb = GaussianNB()

modelo_nb.fit(X_train, y_train)

predicciones_nb = modelo_nb.predict(X_test)
precision_nb = accuracy_score(y_test, predicciones_nb)

print("--- Algoritmo Naive Bayes ---")
print(f"Precisión basada en probabilidad: {precision_nb * 100:.2f}%")