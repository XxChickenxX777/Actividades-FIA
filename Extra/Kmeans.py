import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()

X_visual = iris.data[:, :2] 

modelo_kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

etiquetas_kmeans = modelo_kmeans.fit_predict(X_visual)

print("--- Algoritmo K-Means ---")
print("Generando gráfica de agrupamiento (Clusters)...")

plt.figure(figsize=(8, 6))
plt.scatter(X_visual[:, 0], X_visual[:, 1], c=etiquetas_kmeans, cmap='viridis', edgecolor='k')

centroides = modelo_kmeans.cluster_centers_
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='X', s=200, label='Centroides')

plt.title('Agrupamiento con K-Means')
plt.xlabel('Longitud del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.legend()
plt.show()