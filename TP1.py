import sys

class EnteroMutable:
    def __init__(self, valor):
        self.valor = valor

    def sumar(self, cantidad=1):
        self.valor += cantidad
    
    def devolver_valor(self):
        return self.valor 

def leer_monedas_de_archivo(archivo):
    
    monedas = []
    try:
        with open(archivo, 'r') as elementos:
            
            for linea in elementos:
                linea = linea.strip() 
                
                if linea.startswith('#'):
                    continue
                
                monedas_en_linea = linea.split(';')
                
                monedas.extend([int(moneda) for moneda in monedas_en_linea])
            
            return monedas
       
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encuentra.")
        return []
    except ValueError:
        print("Error: Asegúrate de que todos los valores en el archivo son números enteros válidos.")
        return []

def moneda_inicial_es_mayor(monedas, inicio, fin):
   return (monedas[inicio] >= monedas[fin])

def seleccionar_moneda(monedas, inicio, fin, jugador, puntos_sofia, puntos_mateo, archivo):
   
    if jugador % 2 != 0:
        if moneda_inicial_es_mayor(monedas, inicio.devolver_valor(), fin.devolver_valor()):
            puntos_sofia.sumar(monedas[inicio.devolver_valor()])
            archivo.write(f"Primera moneda para Sophia ({monedas[inicio.devolver_valor()]});\n")
            inicio.sumar()
        else: 
            puntos_sofia.sumar(monedas[fin.devolver_valor()])
            archivo.write(f"Última moneda para Sophia ({monedas[fin.devolver_valor()]});\n")
            fin.sumar(-1)
    else:
        if moneda_inicial_es_mayor(monedas, inicio.devolver_valor(), fin.devolver_valor()):
            puntos_mateo.sumar(monedas[fin.devolver_valor()])
            archivo.write(f"Última moneda para Mateo ({monedas[fin.devolver_valor()]});\n")
            fin.sumar(-1)
        else: 
            puntos_mateo.sumar(monedas[inicio.devolver_valor()])
            archivo.write(f"Primera moneda para Mateo ({monedas[inicio.devolver_valor()]});\n")
            inicio.sumar()
       
def jugar(monedas):
    inicio = EnteroMutable(0)
    fin = EnteroMutable(len(monedas) - 1)
    puntos_sofia = EnteroMutable(0)
    puntos_mateo = EnteroMutable(0)

    with open('resultado.txt', 'w') as archivo:
        for i in range(len(monedas)):
            seleccionar_moneda(monedas, inicio, fin, i+1, puntos_sofia, puntos_mateo, archivo)

        archivo.write(f"\nResultado final:\n")
        archivo.write(f"Puntos Sofía: {puntos_sofia.devolver_valor()}\n")
        archivo.write(f"Puntos Mateo: {puntos_mateo.devolver_valor()}")


if __name__ == "__main__":
  
    if len(sys.argv) < 2:
        print("Error: Por favor, proporciona el nombre del archivo como parámetro.")
        sys.exit(1)
    
    archivo = sys.argv[1]

    monedas = leer_monedas_de_archivo(archivo)
    
    if monedas: jugar(monedas)