# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    personas = []

    with open(filename, 'r') as archivo:
        lineas = []

        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                lineas.append(linea)

        if len(linea) <= 1:
            return []

        header = linea[0].split(',')

        for linea in lineas[1:]:
            valores = linea.split(',')
            persona = {}

            for i in range(len(header)):
                clave = header[i].strip()
                valor = valores[i].strip()

                if clave == "age":
                    valor = int(valor)

                persona[clave] = valor

            personas.append(persona)

    return personas

