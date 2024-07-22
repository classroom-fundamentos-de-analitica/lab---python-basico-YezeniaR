"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.
"""


def pregunta_01():
    nombre_archivo = "data.csv"
    suma = 0
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split()
            if len(columnas) > 1:
                suma += int(columnas[1])
    return suma


def pregunta_02():
    nombre_archivo = "data.csv"
    registros_por_letra = {}

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            letra = linea[0]
            if letra not in registros_por_letra:
                registros_por_letra[letra] = 0
            registros_por_letra[letra] += 1

    lista_tuplas = sorted([(letra, cantidad) for letra, cantidad in registros_por_letra.items()])
    return lista_tuplas


def pregunta_03():
    nombre_archivo = "data.csv"
    sumas = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            valores = linea.strip().split()
            letra, valor = valores[0], int(valores[1])
            if letra in sumas:
                sumas[letra] += valor
            else:
                sumas[letra] = valor
    resultado = sorted(sumas.items())
    return resultado


def pregunta_04():
    nombre_archivo = "data.csv"
    meses = {}
    archivo = open(nombre_archivo, 'r')
    registros = archivo.readlines()

    for registro in registros:
        datos = registro.strip().split('\t')
        fecha=datos[2]
        mes = fecha.split('-')[1]
        if mes not in meses:
            meses[mes] = 1
        else:
            meses[mes] += 1

    lista_meses= sorted([(mes, cantidad) for mes, cantidad in meses.items()])
    return lista_meses


def pregunta_05():
    nombre_archivo = "data.csv"
    archivo = open(nombre_archivo, 'r')
    registros = archivo.readlines()

    max_min_valores = {}
    for registro in registros:
        datos = registro.strip().split('\t')
        letra = datos[0]
        valor = int(datos[1])
        if letra not in max_min_valores:
            max_min_valores[letra] = (valor, valor)
        else:
            max_val, min_val = max_min_valores[letra]
            max_val = max(max_val, valor)
            min_val = min(min_val, valor)
            max_min_valores[letra] = (max_val, min_val)

    resultado = []
    for letra, (max_val, min_val) in max_min_valores.items():
        resultado.append((letra, max_val, min_val))
    resultado=sorted(resultado )
    return resultado


def pregunta_06():
  nombre_archivo = "data.csv"
  resultados = {}

  with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split()

            if len(columnas) >= 5:
                clave_valor = columnas[4].split(',')
                
                for cv in clave_valor:
                    clave, valor = cv.split(':')
                    valor = int(valor)

                    if clave in resultados:
                        min_valor, max_valor = resultados[clave]
                        resultados[clave] = (min(min_valor, valor), max(max_valor, valor))
                    else:
                        resultados[clave] = (valor, valor)

  lista_resultados = sorted([(clave, min_valor, max_valor) for clave, (min_valor, max_valor) in resultados.items()])

  return lista_resultados


def pregunta_07():
    nombre_archivo = "data.csv"
    resultados = {}

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split('\t')

            if len(columnas) >= 5:
                letras = columnas[0].split(',')
                valor_columna2 = int(columnas[1])

                if valor_columna2 in resultados:
                    resultados[valor_columna2].extend(letras)
                else:
                    resultados[valor_columna2] = letras

    lista_resultados = sorted([(clave, valores) for clave, valores in resultados.items()])

    return (lista_resultados)


def pregunta_08():
    nombre_archivo = "data.csv"
    resultados = {}

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split()

            if len(columnas) >= 2:
                valor = int(columnas[1])
                letras = columnas[0].split(',')

                if valor in resultados:
                    for letra in letras:
                        resultados[valor].add(letra)
                else:
                    resultados[valor] = set(letras)

    lista_resultados = sorted([(valor, sorted(letras)) for valor, letras in resultados.items()])

    return lista_resultados


def pregunta_09():
    nombre_archivo = "data.csv"
    registros = {}

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split()

            if len(columnas) >= 5:
                clave_valor = columnas[4].split(',')

                for cv in clave_valor:
                    clave, _ = cv.split(':')

                    if clave in registros:
                        registros[clave] += 1
                    else:
                        registros[clave] = 1
    registros = dict(sorted(registros.items()))
    return registros


def pregunta_10():
    nombre_archivo = "data.csv"
    resultados = []

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split()
            
            if len(columnas) >= 5:
                letra = columnas[0]
                cantidad_columna4 = len(columnas[3].split(','))
                clave_valor = columnas[4].split(',')
                cantidad_columna5 = len(clave_valor)

                resultados.append((letra, cantidad_columna4, cantidad_columna5))

    return resultados


def pregunta_11():
    nombre_archivo = "data.csv"
    resultados = {}

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split()

            if len(columnas) >= 4:
                letras = columnas[3].split(',')

                for letra in letras:
                    if letra in resultados:
                        resultados[letra] += int(columnas[1])
                    else:
                        resultados[letra] = int(columnas[1])

    resultados_ordenados = dict(sorted(resultados.items()))

    return resultados_ordenados


def pregunta_12():
    nombre_archivo = "data.csv"
    diccionario = {}

    with open(nombre_archivo, 'r') as f:
        for linea in f:
            columnas = linea.split('\t')

            if len(columnas) >= 5:
                clave = columnas[0]
                valor_columna5 = columnas[4].strip().split(',')

                for valor in valor_columna5:
                    clave_valor = valor.split(':')
                    if len(clave_valor) == 2:
                        _, valor = clave_valor
                        diccionario.setdefault(clave, 0)
                        diccionario[clave] += int(valor)

    resultados_ordenados = dict(sorted(diccionario.items()))
    return resultados_ordenados
