from random import seed

from matplotlib import pyplot as plt 
import seaborn as sns 
import numpy as np 
import scipy as sp 
import statistics

from TP1 import jugar
from medidor_comp_temp import medidor_de_complejidad_temporal
 
# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)
sns.set_theme()

# Configuración de los tamaños de lista y repeticiones
tamanios_de_lista_x = np.arange(20, 10000 , 1000)  # Tamanios de lista de 20 a 10000
tiempos_de_ejecucion = []

# Calculamos los distintos valores medios de tiempos para cada tamanio de la lista y los guardamos en lista:tiempos_de_ejecucion
for tamanio in tamanios_de_lista_x:
    sample_list = np.random.randint(0, 1000, size=tamanio).tolist() #lista con números aleatorios
    valor_tiempo_medio = medidor_de_complejidad_temporal(jugar, sample_list, repeticiones=20)
    tiempos_de_ejecucion.append(valor_tiempo_medio)

# Instrucciones que grafican los resultados
plt.plot(tamanios_de_lista_x, tiempos_de_ejecucion, marker='o', linestyle='-', color='b')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempo de Ejecución de jugar en función del Tamaño de la Lista')
plt.grid(True)
plt.show()

#Cuadrados minimos
A = np.array([[tamanio, 1] for tamanio in tamanios_de_lista_x])
b = np.array(tiempos_de_ejecucion)
b = b[:, np.newaxis]
AtA = A.T @ A
Atb = A.T @ b
c = np.linalg.inv(AtA) @ Atb

print(f"c_1 = {c[0]}, c_2 = {c[1]}")
r = np.linalg.norm(A @ c - b)**2 # || Ax - b ||^2
print(f"Error cuadrático total: {r}") 

#Lo que me devuelve la consola
"""c_1 = [6.45445152e-07], c_2 = [0.00017878]
Error cuadrático total: 7.286458664378666e-07
"""