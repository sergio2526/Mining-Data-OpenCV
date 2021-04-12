from argparse import ArgumentParser
import cv2
import numpy as np 

# Menu del programa
Argument_parser =ArgumentParser()
Argument_parser.add_argument('-i','--input', required=True, help="Ruta de la imagen de entrada")
arguments = vars(Argument_parser.parse_args())

# Leemos la imagen, y la mostramos en pantalla
image = cv2.imread(arguments['input'])
cv2.imshow('Original', image)
cv2.waitKey(0)

# Mediante la función cv2.split() obtenemos los canales de color de la imagen
# Orden de canales BGR 
blue, green, red = cv2.split(image)

#Creamos un mosaico de cada canal de color por separado
color_mosaic = np.hstack([red, green, blue])
cv2.imshow('Rojo |  Verde | Azul', color_mosaic)
cv2.waitKey(0)

# Creando lienzo
empty_canvas = np.zeros_like(blue)


# Creamos una imagen de color correspondiente al canal azul, pero coloreado (para ello, dos de los tres canales de la
# foto corresponden al lienzo vacío creado arriba).
blue_colored = cv2.merge([blue, empty_canvas, empty_canvas])

# Creamos una imagen de color correspondiente al canal verde, pero coloreado (para ello, dos de los tres canales de la
# foto corresponden al lienzo vacío creado arriba).
green_colored = cv2.merge([empty_canvas, green, empty_canvas])

# Creamos una imagen de color correspondiente al canal rojo, pero coloreado (para ello, dos de los tres canales de la
# foto corresponden al lienzo vacío creado arriba).
red_colored = cv2.merge([empty_canvas, empty_canvas, red])


# Creamos un mosaico de los canales coloreados para luego mostrarlo en pantalla.
colored_mosaic = np.hstack([blue_colored, green_colored, red_colored])
cv2.imshow('Rojo | Verde | Azul (Coloreado)', colored_mosaic)
cv2.waitKey(0)


# Finalmente, reconstruimos la imagen original, con ayuda de la función cv2.merge(), a la cual le pasamos los canales
# de color en el orden adecuado (BGR),
original_reconstructed = cv2.merge([blue, green, red])
cv2.imshow('Original (reconstruida)', original_reconstructed)
cv2.waitKey(0)