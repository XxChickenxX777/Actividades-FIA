import numpy as np
import matplotlib.pyplot as plt
import time

def ejecutar_kmeans():
    np.random.seed(42)
    grupo1 = np.random.normal(loc=[2, 2], scale=0.6, size=(40, 2))
    grupo2 = np.random.normal(loc=[8, 8], scale=0.6, size=(40, 2))
    grupo3 = np.random.normal(loc=[2, 8], scale=0.6, size=(40, 2))
    coordenadas = np.vstack((grupo1, grupo2, grupo3))

    k = 3
    indices = [
        np.random.randint(0, 40),     
        np.random.randint(40, 80),    
        np.random.randint(80, 120)
    ]
    centroides = coordenadas[indices]

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.canvas.manager.set_window_title('Plataforma LifeLink - Simulación (Feb-Marzo)')

    for paso in range(15):
        ax.clear()
        
        distancias = np.linalg.norm(coordenadas[:, np.newaxis] - centroides, axis=2)
        etiquetas = np.argmin(distancias, axis=1)
        
        ax.scatter(coordenadas[:, 0], coordenadas[:, 1], c=etiquetas, cmap='viridis', alpha=0.6, s=50)
        ax.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='X', s=200, edgecolors='black', linewidths=2)
        
        ax.set_title(f'Buscando el centro óptimo... Iteración {paso + 1}', fontsize=14)
        ax.grid(True, linestyle='--', alpha=0.5)
        
        plt.draw()
        plt.pause(1.5)
        
        nuevos_centroides = np.array([coordenadas[etiquetas == i].mean(axis=0) for i in range(k)])
        
        if np.all(centroides == nuevos_centroides):
            ax.set_title(f'¡Convergencia alcanzada en la iteración {paso + 1}!', fontsize=14, color='green')
            plt.draw()
            plt.pause(3)
            break
            
        centroides = nuevos_centroides

    plt.ioff()
    plt.show()

ejecutar_kmeans()