# CodigosCorrectores

Tres programas en Python. El primero, que llamaremos codificar, recibe un texto y pasa ese textos a ceros y unos utilizando el código ascii extendido. A continuación pasa esos ceros y unos a un nuevo listado de ceros y unos pero que está formado por palabras del código que se ha asignado a cada alumno (código sobre el cuerpo de 16 elementos, cada elemento de este cuerpo formado por cuatro ceros y unos, y cada palabra del código formado por varuios elementos del cuerpo) y por último almacena ese listado en un fichero de texto.

El segundo, que llamaremos corregir, recibe un fichero de texto, formado sólo por ceros y unos, y da como salida un nuevo fichero de texto, también formado unicamente por ceros y unos, pero ahora formado por palabras del código. Si el alumno tiene asignado un código de longitud n, divide el fichero que recibe el bloques de 4n ceros y uno y cada uno de esos bloques lo sustituye por una palabra del código (si hay alguna a distancia que se puede corregir, lo sustituirá por esa)..

El tercero y último lo llamaremos decodificar. Recibe un fichero de texto que contiene ceros y unos y está formado por palabras del código.Convierte esas palabras del código en elementos del código ascii y devuelve el texto con que esos elementos del código ascii se corresponden.
