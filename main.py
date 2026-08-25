# importamos la libreria requests para realizar la peticion web
import requests
# importamos bs4 para extraer y analizar el codigo html
import bs4

# guardamos la url objetivo dentro de una variable de texto
url = "https://www.cespe.gob.mx/public/"

# definimos un encabezado para simular la visita desde un navegador web
headers = {'user-agent': 'mozilla/5.0'}

# intentamos realizar la descarga de la pagina y el procesamiento de datos
try:
    # realizamos la peticion get a la pagina web usando requests
    respuesta = requests.get(url, headers=headers)

    # obtenemos y procesamos el contenido html con bs4
    soup = bs4.BeautifulSoup(respuesta.text, 'html.parser')

    # buscamos y extraemos todo el texto visible del sitio web
    texto_pagina = soup.get_text()

    # limpia caracteres de puntuacion comunes para separar mejor las palabras
    texto_limpio = texto_pagina.replace(',', '').replace('.', '').replace(';', '')

    # separamos el texto completo en una lista de palabras
    texto_separado = texto_limpio.split()
    # obtenemos la cantidad total de palabras encontradas
    texto_size = len(texto_separado)

    # definimos la lista con los dias de la semana en minusculas y sin acentos
    dias_semana = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]

    # definimos las palabras clave para identificar ubicaciones
    tipos_ubicacion = ["calle", "colonia", "col", "avenida", "av"]

    # creamos los diccionarios vacios
    diccionario_dias = {}
    diccionario_ubicaciones = {"calle": [], "colonia": [], "avenida": []}

    # recorremos la lista palabra por palabra usando su indice
    for i in range(0, texto_size):
        # convertimos la palabra actual a minusculas para evaluarla
        palabra_actual = texto_separado[i].lower()

        # evaluacion de dias de la semana y sus digitos
        if palabra_actual in dias_semana:
            # verificamos que exista una palabra siguiente en la lista
            if i + 1 < texto_size:
                # tomamos la siguiente palabra que deberia contener el numero
                siguiente_palabra = texto_separado[i + 1]

                # comprobamos si la palabra siguiente esta compuesta solo por digitos
                if siguiente_palabra.isdigit():
                    # convertimos la cadena de texto a un numero entero
                    numero = int(siguiente_palabra)

                    # evaluamos si el numero esta estrictamente en el rango de 1 a 31
                    if 1 <= numero <= 31:
                        # guardamos el numero en el diccionario asociándolo al dia
                        diccionario_dias.setdefault(palabra_actual, []).append(numero)

        #identificacion de calles, colonias y avenidas
        if palabra_actual in tipos_ubicacion:
            # verificamos que exista una palabra siguiente para el nombre
            if i + 1 < texto_size:
                # tomamos la palabra siguiente como nombre de la ubicacion
                nombre_ubicacion = texto_separado[i + 1].lower()

                # clasificamos segun el tipo de ubicacion encontrado
                if palabra_actual == "calle":
                    diccionario_ubicaciones["calle"].append(nombre_ubicacion)
                elif palabra_actual in ["colonia", "col"]:
                    diccionario_ubicaciones["colonia"].append(nombre_ubicacion)
                elif palabra_actual in ["avenida", "av"]:
                    diccionario_ubicaciones["avenida"].append(nombre_ubicacion)

    #impresion de resultados

    # mostramos en pantalla el diccionario de dias y sus digitos evaluados
    print("--- diccionario de dias y digitos (1-31) ---")
    print(diccionario_dias)

    # mostramos en pantalla el diccionario de ubicaciones guardadas
    print("\n--- diccionario de ubicaciones extraidas ---")
    print(diccionario_ubicaciones)

# capturamos posibles errores durante la ejecucion
except Exception as e:
    # mostramos un mensaje explicativo si algo falla
    print(f"ocurrio un error durante la ejecucion: {e}")
