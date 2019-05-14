# -*- coding:utf-8 -*-
from codificar import comprobarTxt, escogerMatriz
import sys

""""Devuelve el caracter del alfabeto ascii extendido correspondiente al número binario que recibe"""
def asciiLetra(letra):
    letra = chr(int(letra,2))
    return letra

"""Decodifica un fichero txt pasando su contenido de estar codificado mediante nuestro código a ascii extendido"""
def decodificar(lectura,escritura):
    dirFicLec = comprobarTxt(lectura)
    try:
        ficheroLec = open(dirFicLec)
    except:
        print('El fichero ' + dirFicLec + ' no existe.')
        sys.exit()
    dirFicEsc = comprobarTxt(escritura)
    ficheroEsc = open(dirFicEsc, 'w')
    while True:
        relleno = ficheroLec.read((len(generatriz[0]) - len(generatriz))*4)
        if not relleno:
            break
        for _ in range(len(generatriz)//2):
            letra = ficheroLec.read(8)
            ficheroEsc.write(asciiLetra(letra))
    ficheroLec.close()
    ficheroEsc.close()
    print('->Fin<-')

if __name__ == "__main__":

    matrices = escogerMatriz()

    generatriz = matrices[0]
    control = matrices[1]

    lectura = str(input("Escriba el nombre del fichero de lectura: "))
    escritura = str(input("Escriba el nombre del fichero de escritura: "))
    
    decodificar(lectura,escritura)