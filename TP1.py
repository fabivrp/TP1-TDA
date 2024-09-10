class EnteroMutable:
    def __init__(self, valor):
        self.valor = valor

    def sumar(self, cantidad=1):
        self.valor += cantidad
    
    def devolver_valor(self):
        return self.valor 



def moneda_inicial_es_mayor(monedas, inicio, fin):
   return (monedas[inicio] >= monedas[fin])


def seleccionar_moneda(monedas, inicio, fin, jugador, puntos_sofia, puntos_mateo):
   
    if jugador % 2 != 0:
        if moneda_inicial_es_mayor(monedas, inicio.devolver_valor(), fin.devolver_valor()):
            puntos_sofia.sumar(monedas[inicio.devolver_valor()])
            inicio.sumar()
        else: 
            puntos_sofia.sumar(monedas[fin.devolver_valor()])
            fin.sumar(-1)
    else:
        if moneda_inicial_es_mayor(monedas, inicio.devolver_valor(), fin.devolver_valor()):
            puntos_mateo.sumar(monedas[fin.devolver_valor()])
            fin.sumar(-1)
        else: 
            puntos_mateo.sumar(monedas[inicio.devolver_valor()])
            inicio.sumar()
       
  

def jugar(monedas):
    inicio = EnteroMutable(0)
    fin = EnteroMutable(len(monedas) - 1)
    puntos_sofia = EnteroMutable(0)
    puntos_mateo = EnteroMutable(0)


    for i in range (1, len(monedas) + 1):
        seleccionar_moneda(monedas, inicio, fin, i, puntos_sofia, puntos_mateo)
  
  
    print(f"Puntos sofi: {puntos_sofia.devolver_valor()}")
    print(f"Puntos mateo: {puntos_mateo.devolver_valor()}")


if __name__ == "__main__":

    monedas =[406,691,451,628,950,324,906,34,345,647,589,585,728,338,598,362,999,227,248,863,852,344,166,153,778]
    jugar(monedas)