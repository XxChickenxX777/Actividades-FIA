import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [
  {"peso": 7.2, "altura": 50, "velocidad": 10.3, "color": "Blanco"},
  {"peso": 8.5, "altura": 66, "velocidad": 10.3, "color": "Amarillo"},
  {"peso": 9.8, "altura": 73, "velocidad": 10.2, "color": "Verde"},
  {"peso": 6.5, "altura": 72, "velocidad": 16.4, "color": "Verde"},
  {"peso": 7.5, "altura": 81, "velocidad": 18.8, "color": "Verde"},
  {"peso": 10.1, "altura": 73, "velocidad": 19.7, "color": "Verde"},
  {"peso": 11.0, "altura": 66, "velocidad": 15.6, "color": "Blanco"},
  {"peso": 11.0, "altura": 75, "velocidad": 21.2, "color": "Amarillo"},
  {"peso": 11.1, "altura": 70, "velocidad": 22.6, "color": None}, # NA
  {"peso": 11.2, "altura": 75, "velocidad": 19.9, "color": "Blanco"},
  {"peso": 11.3, "altura": 69, "velocidad": 24.2, "color": "Amarillo"},
  {"peso": 11.4, "altura": 76, "velocidad": 21.0, "color": "Blanco"},
  {"peso": 11.4, "altura": 76, "velocidad": 21.4, "color": "Verde"},
  {"peso": 11.7, "altura": 69, "velocidad": 21.3, "color": "Verde"},
  {"peso": 12.0, "altura": 75, "velocidad": np.nan, "color": "Amarillo"}, # NA
  {"peso": 12.9, "altura": 64, "velocidad": 22.2, "color": "Amarillo"},
  {"peso": 12.9, "altura": 55, "velocidad": 33.8, "color": "Blanco"},
  {"peso": 10.3, "altura": 76, "velocidad": 27.4, "color": "Amarillo"},
  {"peso": 9.7, "altura": 71, "velocidad": 25.7, "color": "Verde"},
  {"peso": 10.8, "altura": 64, "velocidad": 24.9, "color": "Verde"},
  {"peso": 11.0, "altura": 78, "velocidad": 23.1, "color": "Amarillo"},
  {"peso": 10.2, "altura": 70, "velocidad": 31.7, "color": "Amarillo"},
  {"peso": 10.5, "altura": 74, "velocidad": 36.3, "color": "Verde"},
  {"peso": 6.5, "altura": 72, "velocidad": 38.3, "color": "Verde"},
  {"peso": 6.3, "altura": 77, "velocidad": 42.6, "color": "Verde"},
  {"peso": 7.3, "altura": 51, "velocidad": 55.4, "color": "Blanco"},
  {"peso": 7.5, "altura": 62, "velocidad": np.nan, "color": "Blanco"}, # NA
  {"peso": 7.9, "altura": 60, "velocidad": 58.3, "color": "Amarillo"},
  {"peso": 8.2, "altura": 70, "velocidad": np.nan, "color": "Verde"} # NA
]

df = pd.DataFrame(data)

print("="*40)
print("MEDIDAS DE TENDENCIA CENTRAL")
print("="*40)
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        print(f"{col.capitalize()}: Media={df[col].mean():.2f}, Mediana={df[col].median():.2f}, Moda={df[col].mode()[0]:.2f}")
    else:
        print(f"{col.capitalize()}: Moda={df[col].mode()[0]}")

print("\n")

peso_bins = pd.cut(df['peso'], bins=5)
peso_freq = peso_bins.value_counts().sort_index().reset_index()
peso_freq.columns = ['Intervalo_Peso', 'Frecuencia_Absoluta']
peso_freq['Frecuencia_Relativa_%'] = (peso_freq['Frecuencia_Absoluta'] / len(df) * 100).round(2)
peso_freq['Frecuencia_Acumulada'] = peso_freq['Frecuencia_Absoluta'].cumsum()

print("TABLA DE FRECUENCIAS: PESO")
print(peso_freq.to_string(index=False))
print("\n")

color_freq = df['color'].dropna().value_counts().reset_index()
color_freq.columns = ['Color', 'Frecuencia_Absoluta']
total_color = color_freq['Frecuencia_Absoluta'].sum()
color_freq['Frecuencia_Relativa_%'] = (color_freq['Frecuencia_Absoluta'] / total_color * 100).round(2)
color_freq['Frecuencia_Acumulada'] = color_freq['Frecuencia_Absoluta'].cumsum()

print("TABLA DE FRECUENCIAS: COLOR")
print(color_freq.to_string(index=False))

plt.figure(figsize=(18, 10))
plt.style.use('seaborn-v0_8-whitegrid')

plt.subplot(2, 3, 1)
plt.bar(peso_freq['Intervalo_Peso'].astype(str), peso_freq['Frecuencia_Absoluta'], color='skyblue', edgecolor='black')
plt.title('Gráfica de Barras: Frec. Absoluta (Peso)', fontsize=12)
plt.xticks(rotation=25)
plt.ylabel('Frecuencia')

plt.subplot(2, 3, 2)
midpoints = peso_freq['Intervalo_Peso'].apply(lambda x: x.mid).astype(float)
plt.plot(midpoints, peso_freq['Frecuencia_Absoluta'], marker='o', color='red', linestyle='-', linewidth=2)
plt.fill_between(midpoints, peso_freq['Frecuencia_Absoluta'], color='red', alpha=0.1)
plt.title('Polígono de Frecuencias (Peso)', fontsize=12)
plt.xlabel('Punto Medio del Intervalo')
plt.ylabel('Frecuencia')

plt.subplot(2, 3, 3)
plt.pie(peso_freq['Frecuencia_Relativa_%'], labels=peso_freq['Intervalo_Peso'].astype(str), autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
plt.title('Diagrama de Pastel: Frec. Relativa (Peso)', fontsize=12)

plt.subplot(2, 3, 4)
colores_barras = ['#4CAF50', '#FFEB3B', '#E0E0E0']
plt.bar(color_freq['Color'], color_freq['Frecuencia_Absoluta'], color=colores_barras, edgecolor='black')
plt.title('Gráfica de Barras: Frec. Absoluta (Color)', fontsize=12)
plt.ylabel('Frecuencia')

plt.subplot(2, 3, 5)
plt.plot(color_freq['Color'], color_freq['Frecuencia_Absoluta'], marker='s', color='purple', linestyle='dashed', linewidth=2)
plt.title('Polígono de Frecuencias (Color)', fontsize=12)
plt.ylabel('Frecuencia')

plt.subplot(2, 3, 6)
plt.pie(color_freq['Frecuencia_Relativa_%'], labels=color_freq['Color'], autopct='%1.1f%%', startangle=90, colors=colores_barras, wedgeprops={'edgecolor': 'black'})
plt.title('Diagrama de Pastel: Frec. Relativa (Color)', fontsize=12)

plt.tight_layout()
plt.show()