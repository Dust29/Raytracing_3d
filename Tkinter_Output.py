
import tkinter as tk
from PIL import Image, ImageTk

def output(rgb_values, width, height):
    # Fonction pour créer une image à partir d'une liste de listes de valeurs RGB
    def create_image_from_list(rgb_list, width, height):
        # Créer une nouvelle image RGB vide
        image = Image.new("RGB", (width, height))

        # Convertir la liste de couleurs en pixels
        pixels = image.load()

        for i in range(width):
            for j in range(height):
                # Affecter la couleur du pixel depuis la liste 2D rgb_list[i][j]
                pixels[i, j] = tuple(rgb_list[i][j])

        return image

    # Création de la fenêtre Tkinter
    Window = tk.Tk()
    Window.title("Image 1920x1080 basée sur une liste de couleurs")
    Window.geometry(f"{width}x{height}")  # Pour s'assurer que l'image ne soit pas déformer



    # Création de l'image à partir de la liste de couleurs
    img = create_image_from_list(rgb_values, width, height)  # Avec PIL, idk

    # Conversion de l'image en objet Tkinter
    tk_image = ImageTk.PhotoImage(img)

    # Création d'un canvas et affichage de l'image
    canvas = tk.Canvas(Window, width=width, height=height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    Window.mainloop()