def moneda_inicial_es_mayor(monedas, inicio, fin):
   return (monedas[inicio] >= monedas[fin])

def seleccionar_moneda(monedas, indices, jugador):
   
    if jugador % 2 != 0:
        if moneda_inicial_es_mayor(monedas, indices[0], indices[1]):
            moneda_seleccionada = monedas[indices[0]]
            indices[0] += 1
        else: 
            moneda_seleccionada = monedas[indices[1]] 
            indices[1] -= 1
    else:
        if moneda_inicial_es_mayor(monedas, indices[0], indices[1]):
            moneda_seleccionada = monedas[indices[1]]
            indices[1] -= 1
        else: 
            moneda_seleccionada = monedas[indices[0]]
            indices[0] += 1
          
    return (moneda_seleccionada)


def jugar(monedas):
    inicio = 0
    fin = len(monedas) - 1
    indices = [inicio, fin]
    puntos_sofi = 0
    puntos_mateo = 0
    for i in range(1, len(monedas)):
        valor_moneda = seleccionar_moneda(monedas, indices, i)
        if i % 2 != 0:
            puntos_sofi += valor_moneda
        else:
            puntos_mateo += valor_moneda    
  
    print(f"Puntos sofi: {puntos_sofi}")
    print(f"Puntos mateo: {puntos_mateo}")


if __name__ == "__main__":
   
    monedas = [72,165,794,892,880,341,882,570,679,725,979,375,459,603,112,436,587,699,681,83]
    jugar(monedas)