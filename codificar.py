# -*- coding:utf-8 -*-
import sys
####################################################################################################################################################
##################################operaciones.py####################################################################################################
####################################################################################################################################################

alphas = ['0000','0010','0100','1000',
          '0011','0110','1100','1011',
          '0101','1010','0111','1110',
          '1111','1101','1001','0001']

"""Suma realizada en el cuerpo de F16"""
def suma(vector,palabra):
    resultado = ''

    for i in range(len(vector)):
        if(vector[i]==palabra[i]):
            resultado = resultado + '0'
        else:
            resultado = resultado + '1'
    return resultado

"""Multiplicación realizada en el cuerpo de F16"""
def mult(vector,palabra):
    global alphas
    if(vector == alphas[0] or palabra == alphas[0]):
        resultado = 0
    else:
        resultado = (alphas.index(vector) + alphas.index(palabra)) % (len(alphas) - 1)
        if(resultado == 0):
            resultado = 15

    return alphas[resultado]

##################################################################################################################################################
##################################matirices.py####################################################################################################
##################################################################################################################################################

generatriz0 = [['0010','0011','0001','0000','0000','0000'],
               ['0110','0111','0000','0001','0000','0000'],
               ['1110','1111','0000','0000','0001','0000'],
               ['1101','1100','0000','0000','0000','0001']]

generatriz1 = [['0010','0011','0001','0000'],
                ['0110','0111','0000','0001']]

generatriz2=[["1100", "0001", "0011", "1111", "0001", "0000"],
             ["1000", "0011", "0011", "1001", "0000", "0001"]]

control0 = [['0001','0001','0001','0001','0001','0001'],
            ['0001','0010','0100','1000','0011','0110']]

control1 = [['0001','0001','0001','0001'],
            ['0001','0011','0111','1111']]

control2 = [["0001", "0001", "0001", "0001", "0001", "0001"],
            ["0001", "0010", "0100", "1000", "0011", "0110"],
            ["0001", "0100", "0011", "1100", "0101", "0111"],
            ["0001", "1000", "1100", "1010", "1111", "0001"]]


"""Imprime un array bidimensional en la forma habitual de representar matrices"""
def printMat(mat):

    for i in range(len(mat)):
        print()
        for j in range(len(mat[i])):
            print(mat[i][j],end=' ')
    print()

"""Multiplica dos arrays bidimensionales en la forma habitual en la que se multiplican matrices"""
def multMat(mat1,mat2):
    matRes = []
    vacio = ''
    if(len(mat1[0]) != len(mat2)):
        print('La matriz')
        printMat(mat1)
        print('y la matriz')
        printMat(mat2)
        print('no se pueden mutiplicar')
    
    for i in alphas[0]:
        vacio += '0'
    for x in range(len(mat1)):
        matRes.append([])
        for _ in range(len(mat2[0])):
            matRes[x].append(vacio)
            
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                if(k == 0):
                    matRes[i][j] = mult(mat1[i][k],mat2[k][j])
                else:
                    matRes[i][j] = suma(matRes[i][j],mult(mat1[i][k],mat2[k][j]))
    
    return matRes

"""Pasa de un string compuesto por n elementos del cuerpo de F16 a un array bidimensional de tamaño 1Xn"""
def vecMat(vector):
    mat = []
    vec = []
    
    for i in range(len(vector)//4):
        y = i * 4
        palabra = vector[y:(y+4)]
        vec.append(palabra)
    mat.append(vec)

    return mat

"""Pasa de un string compuesto por n elementos del cuerpo de F16 a un array bidimensional de tamaño nX1"""
def palabraMatriz(palabra):
    mat = []
    
    for i in range(len(palabra)//4):
        y = i * 4
        res = palabra[y:(y+4)]
        mat.append([res])

    return mat

"""Multiplica un vector por la matriz generatriz para obtener así la imagen en el código de dicha matriz y devuelve dicha imagen"""
def imagen(vector):
    mat = multMat(vecMat(vector), generatriz)
    imagen = vectorToString(mat)
    return imagen
    
"""Devuelve un string compuesto por los elementos de un array bidimensional 1Xn"""
def vectorToString(vector):
    vectorString = ''
    
    for i in vector[0]:
        vectorString = vectorString + i
        
    return vectorString

"""Traspone una matriz bidimensional nx1"""
def trasponerMatriz(vector):
    mat = [[]]
    
    for i in range(len(vector)):
        mat[0].append(vector[i][0])
    
    return mat

##################################################################################################################################################
##################################codificar.py####################################################################################################
##################################################################################################################################################

"""Devuelve el caracter ascii codificado en binario"""
def letraAscii(letra):
    valor = bin(ord(letra))
    
    valor = valor[2:]
    while(len(valor) < 8):
        valor = '0' + valor
    return valor

"""Devuelve la codificación de la palabra compuesta por 2 caracteres ascii"""
def asciiCodigo(palabra):
    palabraCod = imagen(palabra)
    return palabraCod

"""Comprueba la terminación del nombre de fichero txt introducido, devuelve siempre el nombre del archivo terminado en .txt"""
def comprobarTxt(fichero):
    longitud = len(fichero)
    terminacion = fichero[(longitud - 4):longitud]
    if (terminacion != '.txt'):
        fichero = fichero + '.txt'
    return fichero

"""Codifica un fichero txt pasando su contenido de estar en nuestro lenguaje a estar codificado mediante nuestro código"""
def codificar(lectura,escritura):
    dirFicLec = comprobarTxt(lectura)
    ficheroLec = open(dirFicLec)

    dirFicEsc = comprobarTxt(escritura)
    ficheroEsc = open(dirFicEsc, 'w')
    while True:
        cadena = ficheroLec.read(len(generatriz)//2)
        
        if not cadena:
            break
        palabra=''
        for i in cadena:
            palabra = palabra + letraAscii(i)
        while (len(palabra) < len(generatriz)*4):
            palabra = palabra + 4*'0'
        palabra = asciiCodigo(palabra)
        ficheroEsc.write(palabra)
    ficheroLec.close()
    ficheroEsc.close()
    print('->Fin<-')

def escogerMatriz():
    opt = 3
    matrices = []
    print('\nGeneratriz 0')
    printMat(generatriz0)

    print('\nGeneratriz 1')
    printMat(generatriz1)

    print('\nGeneratriz 2')
    printMat(generatriz2)
    print()

    while(opt != 2 and opt != 1 and opt != 0):
        try:
            opt = int(input('¿Con el código generado por qué matriz quiere trabajar? (0, 1 o 2): '))
        except:
            print('Escriba 0, 1 o 2 por favor.')
    if(opt==0):
        generatriz = generatriz0
        control = control0
    elif (opt==1):
        generatriz = generatriz1
        control = control1
    else:
        generatriz = generatriz2
        control = control2

    matrices.append(generatriz)
    matrices.append(control)
    return matrices
if __name__ == "__main__":
    
    matrices = escogerMatriz()

    generatriz = matrices[0]
    control = matrices[1]

    lectura = str(input("Escriba el nombre del fichero de lectura: "))
    escritura = str(input("Escriba el nombre del fichero de escritura: "))

    codificar(lectura,escritura)

