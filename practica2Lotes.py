################################################
###  Práctica 02: Procesamiento por lotes 2  ###
################################################
# Bibliotecas
import os
import shutil
import random
import string

# Función para copiar y procesar un archivo
def copiar_y_procesar_archivo(origen, destino):
    try:
        # Abrir el archivo de origen en modo lectura
        with open(origen, 'r', encoding='utf-8') as archivo_origen:
            contenido = archivo_origen.read()

        contenido_modificado = ''
        # Iterar a través de cada carácter en el contenido del archivo
        for caracter in contenido:
            if caracter.isalpha():  # Si el carácter es una letra
                contenido_modificado += random.choice(string.digits)  # Reemplazar con un dígito aleatorio
            elif caracter.isdigit():  # Si el carácter es un dígito
                contenido_modificado += random.choice(string.ascii_uppercase)  # Reemplazar con una letra mayúscula aleatoria
            else:
                contenido_modificado += caracter  # Mantener otros caracteres sin cambios

        # Escribir el contenido modificado en el archivo de destino
        with open(destino, 'w', encoding='utf-8') as archivo_destino:
            archivo_destino.write(contenido_modificado)

    except Exception as e:
        print(f"Error al procesar el archivo {origen}: {str(e)}")

# Función para copiar y procesar una carpeta y sus archivos
def copiar_y_procesar_carpeta(origen, destino):
    try:
        # Copiar toda la estructura de carpetas y archivos de origen a destino
        shutil.copytree(origen, destino)

        # Recorrer todos los archivos dentro de la carpeta de destino
        for directorio_raiz, _, archivos in os.walk(destino):
            for archivo in archivos:
                ruta_archivo = os.path.join(directorio_raiz, archivo)
                # Llamar a la función para copiar y procesar cada archivo individualmente
                copiar_y_procesar_archivo(ruta_archivo, ruta_archivo)

    except Exception as e:
        print(f"Error al copiar y procesar la carpeta {origen}: {str(e)}")

if __name__ == "__main__":
    carpeta_origen = "Raiz"  # Ruta de la carpeta original
    carpeta_destino = carpeta_origen + "_copia"  # Ruta de la carpeta destino

    # Llamar a la función para copiar y procesar la carpeta
    copiar_y_procesar_carpeta(carpeta_origen, carpeta_destino)

    # Imprimir un mensaje indicando que la carpeta ha sido copiada y procesada
    print(f"Carpeta copiada y procesada en {carpeta_destino}")
########################################

