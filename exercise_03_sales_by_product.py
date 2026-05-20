# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    """
    Lee un archivo con ventas en formato "producto:valor;producto:valor;..."
    (todo en una sola línea, los registros separados por ';') y agrupa los
    valores en una lista por producto.

    Reglas:
    - Los valores se convierten a float.
    - El orden de los montos dentro de la lista es el mismo en que aparecen
      en el archivo.
    - Los separadores ';' finales sin contenido se ignoran (es común que
      el archivo termine con ';').
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[float]] - montos de venta agrupados por producto.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "producto1:100;producto2:200;producto1:150;"
        read_sales("ventas.txt") -> {
            "producto1": [100.0, 150.0],
            "producto2": [200.0],
        }
    """
resultado = {}
    with open (filename, 'r') as archivo:
        contenido = archivo.read()
    
        partes = contenido.strip()
        partes = partes.split(';')
        
        for parte in partes:
            if parte != "":
                producto, valor = parte.split(':')
                valor = float(valor)
                
                if producto not in resultado:
                    resultado[producto] = [valor]
                elif producto in resultado:
                    resultado[producto].append(valor)
    return resultado

def process_sales(data):
    """
    Para cada producto del diccionario, imprime en el orden natural del dict:

        producto: ventas totales $X.XX, promedio $Y.YY

    Los valores de total y promedio deben mostrarse siempre con DOS
    decimales.

    Args:
        data: dict[str, list[float]] - salida de read_sales.

    Returns:
        None

    Ejemplo:
        process_sales({"producto1": [100.0, 150.0]})
        # imprime: "producto1: ventas totales $250.00, promedio $125.00"
    """

for producto in data:
        total = sum(data[producto])
        promedio = total / len(data[producto])
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

