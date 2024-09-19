
# TP1 - Aplicación de un algoritmo Greedy

## Descripción
Este proyecto tiene como finalidad implementar un algoritmo Greedy para encontrar la solución al problema planteado en la consigna . 
Debe proveerse un archivo .txt que contenga las monedas que se usarán en el juego, el archivo debe seguir un formato específico, 
donde los valores de las monedas están separados por `;`.

## Ejecución

Para ejecutar el programa, debemos hacer lo siguiente:

1. Ubicar la carpeta donde se guardó el proyecto y el archivo contenedor de monedas:

   ```bash
   cd ruta/a/la/carpeta/del/proyecto
   ```

2. Ejecutar utilizando el siguiente comando:

   ```bash
   python -u "ruta/a/TP1.py" archivo_monedas.txt
   ```

   Donde:
   - `ruta/a/TP1.py` es el path al script de Python (ajusta esta ruta de acuerdo a tu directorio local).
   - `archivo_monedas.txt` es el archivo de texto que contiene los valores de las monedas.

   Ejemplo:

   ```bash
   python -u "src/TP1.py" 25.txt
   ```

## Formato del archivo de entrada

El archivo de texto debe contener los valores de las monedas separados por punto y coma `;`. Ejemplo de contenido:

```
332;725;878;918;280;651;45;806;446;422;986;726;592;45;756;280;623;999;78;732;503;680;29;124;450;395;494;749;517;682;11;308;742;697;82;531;197;115
```
