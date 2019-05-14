# -*- coding:utf-8 -*-
from codificar import comprobarTxt, vectorToString, trasponerMatriz, multMat, palabraMatriz, suma, escogerMatriz
import sys

"""Genera los sindromes de los vectores líderes de peso 1 y los devuelve en un diccionario cuya clave es el sindrome y su valor el vector"""
def generaSindromes():
    numeros = []
    sindromes = {}
    vectorLid = palabraMatriz(len(generatriz[0])*4*'0')

    for i in range(1,16):
        numero = bin(i)
        numero = numero[2:]
        while(len(numero) < 4):
            numero = '0' + numero
        numeros.append(numero)
    
    for i in range(len(vectorLid)):
        
        for j in range(15):
            vectorLid[i][0] = numeros[j]
            vector = vectorToString(trasponerMatriz(vectorLid))

            sindrome = vectorToString(trasponerMatriz(multMat(control,vectorLid)))
            sindromes[sindrome] = vector
            vectorLid[i][0] = len(vectorLid[i][0])*'0'
    return sindromes

"""Comprueba el sindrome de una palabra y en base a ello devuelve un vector que sumarle a dicha palabra para corregirlo,
en caso de tener más de un error devuelve un vector formado por asteriscos codificados"""
def comprobar(palabra):
    sindrome = vectorToString(trasponerMatriz(multMat(control,palabraMatriz(palabra))))
    try:
        vector = sindromes[sindrome]
        print('Se ha corregido un error')
    except:
        if(sindrome!=len(control)*4*'0'):
            print('Un error no pudo corregirse')
            vector = asterisco
        else:
            vector = (4*'0')*len(generatriz[0])
    return vector

"""Corrige hasta un error en cada grupo de 6 elementos del cuerpo de un fichero txt y escribe dicha correción en otro fichero"""
def corregir(lectura,escritura):
    dirFicLec = comprobarTxt(lectura)
    try:
        ficheroLec = open(dirFicLec)
    except:
        print('El fichero ' + dirFicLec + ' no existe.')
        sys.exit()
    dirFicEsc = comprobarTxt(escritura)
    ficheroEsc = open(dirFicEsc, 'w')
    while True:
        palabra = ficheroLec.read(len(generatriz[0])*4)
        if not palabra:
            break
        vector = comprobar(palabra)
        if(vector == asterisco):
            palabra = asterisco
        else:
            palabra = suma(vector, palabra)
        ficheroEsc.write(palabra)
    ficheroLec.close()
    ficheroEsc.close()
    print('->Fin<-')



if __name__ == "__main__":

    matrices = escogerMatriz()

    generatriz = matrices[0]
    control = matrices[1]

    sindromes = generaSindromes()

    asterisco = (4*'0')*(len(generatriz)//2) + '00101010'*(len(generatriz)//2)
    
    lectura = str(input("Escriba el nombre del fichero de lectura: "))
    escritura = str(input("Escriba el nombre del fichero de escritura: "))
    
    corregir(lectura,escritura)