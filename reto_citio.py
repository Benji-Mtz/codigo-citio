# GLOBALES
piramide = []
sumatoria = []

nombre_archivo = 'triangulo.txt'


def obtener_piramide_de_enteros(nombre_archivo):
    with open(nombre_archivo) as myfile:
        lineas = myfile.readlines()
        for linea in lineas:
            cadena_sin_saltos = linea.strip('\n')
            cadena_a_lista = cadena_sin_saltos.split(" ")
            lista_de_enteros = [ int(entero) for entero in cadena_a_lista]
            piramide.append(lista_de_enteros)

def obtener_numeros_a_sumar():
    for indice, valor in enumerate(piramide):
        if indice == 0:
            posicion = 0
            sumatoria.append(valor[posicion])
        else:
            posicion_actual = posicion
            posicion_mas_uno = posicion + 1
            if valor[posicion_actual] > valor[posicion_mas_uno]:
                posicion = posicion_actual
                sumatoria.append(valor[posicion_actual])
            elif valor[posicion_mas_uno] > valor[posicion_actual]:
                posicion = posicion_mas_uno
                sumatoria.append(valor[posicion_mas_uno])
                
def suma_mas_alta():
    resultado_sumatoria = sum(sumatoria)
    return resultado_sumatoria

def desglose_suma():
    print(f'La suma maxima de la punta hasta la base es:', end = '')
    for numeros in sumatoria:
        if numeros == sumatoria[len(sumatoria)-1]:
            print(f' {numeros}', end = '')
        else:
            print(f' {numeros} +', end = '')
    print(f' = {suma_mas_alta()}', end = '')
        
        
        
obtener_piramide_de_enteros(nombre_archivo)
obtener_numeros_a_sumar()

suma = suma_mas_alta()
print(f'Suma total: {suma}')

desglose_suma()