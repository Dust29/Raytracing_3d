import Tkinter_Output
import random

# Dimensions de l'image
width, height = 1920, 1080

#TEMPORAIRE
# Création d'une liste de listes de couleurs RGB (structure 2D)
rgb_values = []
for i in range(width):
    row = []
    print(int((i + 1) / width * 100))  # Pour afficher un pourcentage
    for j in range(height):
        # Chaque pixel est une liste [R, G, B]
        row.append(
            [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])  # On rempli de valeurs aléatoires
        # On a donc une liste de liste de liste
        # Rgb_Value[Colonnes[Lignes[Pixel]]]

    rgb_values.append(row)

Tkinter_Output.output(rgb_values,width, height) #Ici, il faudra simplement mettre l'array finit du raytracing pour que tkinter l'affiche
