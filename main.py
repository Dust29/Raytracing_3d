import Tkinter_Output
import random
from Ray_Tracer import Vec3_Class, Color_Utils

# Dimensions de l'image
width, height = 256, 256

# TEMPORAIRE
# Création d'une liste de listes de couleurs RGB (structure 2D)
rgb_values = []
for j in range(height):
    row = []
    print(f'Scanline remaining {height - j}')
    for i in range(width):

        # On défini les couleurs en fonctions des positions (de 0 à 1)
        pixel_color = Color_Utils.color((i / (width-1)), (j / (height - 1)), 0.0)

        row.append(Color_Utils.write_color(pixel_color))

    rgb_values.append(row)


# Ici, il faudra simplement mettre l'array finit du raytracing pour que tkinter l'affiche
Tkinter_Output.output(rgb_values, width, height)
