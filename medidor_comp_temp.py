import time
import matplotlib.pyplot as plt
import numpy as np
import statistics

"""
    Mide el tiempo de ejecución de una función f durante un número de repeticiones.
    :parametros f: La función cuyo tiempo de ejecución queremos medir
    :parametros argumentos_de_funcion_a_medir: Son los argumentos que se pasarán a la función `f`.
    :parametros repeticiones: Número de veces que se ejecutará la función para promediar el tiempo.
    :return: El tiempo medio de ejecución en segundos.
 """
def medidor_de_complejidad_temporal(f, *argumentos_de_funcion_a_medir, repeticiones=20):
    tiempos = []
    for _ in range(repeticiones):
        tiempo_de_inicio = time.perf_counter()  
        f(*argumentos_de_funcion_a_medir)  
        tiempo_de_fin = time.perf_counter()  
        tiempos.append(tiempo_de_fin - tiempo_de_inicio)  # Duración de esta ejecución

    # Calculo el tiempo medio de ejecución
    tiempo_medio = statistics.mean(tiempos)
    return tiempo_medio

