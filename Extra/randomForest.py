from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)

modelo_rf.fit(X_train, y_train)

predicciones_rf = modelo_rf.predict(X_test)
precision_rf = accuracy_score(y_test, predicciones_rf)

print("--- Algoritmo Random Forest ---")
print(f"Precisión del bosque: {precision_rf * 100:.2f}%")