from random import seed
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


from util import time_algorithm 

seed(12345)
np.random.seed(12345)

sns.set_theme()


def get_random_array(size: int):
    return np.random.randint(0, 100_000, size)


    x = np.linspace(100, 10_000_000, 20).astype(int)
    
  
    results = time_algorithm(jugar, x, lambda s: [get_random_array(s)])
    
    
    #Gráfico tiempo de ejecución
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución de jugar')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')
    plt.show()


 
    #Cálculo error 
    A = np.array([[n, 1] for n in x])
    b = np.array([results[size] for size in x])

    AtA = A.T @ A  
    Atb = A.T @ b  
    
    c_manual = np.linalg.solve(AtA, Atb) 
    print(f"Método Manual: c1 = {c_manual[0]}, c2 = {c_manual[1]}")
    

    r_manual = np.linalg.norm(A @ c_manual - b)**2
    print(f"Método Manual: Error cuadrático total = {r_manual}")
    
   
    f_lin_manual = lambda n: c_manual[0] * n + c_manual[1]
    
    #Gráfico tiepo y ajuste
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, b, 'bo', label="Medición")
    ax.plot(x, f_lin_manual(x), 'r--', label=f"Ajuste Lineal Manual: {c_manual[0]:.2e} * n + {c_manual[1]:.2e}")
    ax.set_title('Tiempo de ejecución de jugar (Ajuste Lineal Manual)')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    plt.show()
    
    errors_manual = np.abs(f_lin_manual(x) - b)
    
    #Gráfico error
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, errors_manual, 'm-o')
    ax.set_title('Error Absoluto del Ajuste Lineal Manual')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')
    plt.show()
    
    print(f"\nMétodo Manual: c1 = {c_manual[0]:.2e}, c2 = {c_manual[1]:.2e}, Error Cuadrático = {r_manual:.2e}")
