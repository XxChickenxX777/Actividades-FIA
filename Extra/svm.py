from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_svm = SVC(kernel='linear', random_state=42)

modelo_svm.fit(X_train, y_train)

predicciones_svm = modelo_svm.predict(X_test)
precision_svm = accuracy_score(y_test, predicciones_svm)

print("--- Algoritmo Support Vector Machine (SVM) ---")
print(f"Precisión de las Máquinas de Vectores de Soporte: {precision_svm * 100:.2f}%")