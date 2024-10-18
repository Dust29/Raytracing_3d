import Tkinter_Output
import random
from Ray_Tracer import Ray_tracer_main, Color_Utils, ray

# Dimensions de l'image
width, height = Ray_tracer_main.width, Ray_tracer_main.height


# TEMPORAIRE
# Création d'une liste de listes de couleurs RGB (structure 2D)
rgb_values = []
for j in range(int(width)):
    row = []
    print(f'Scanline remaining {width - j}')
    for i in range(int(height)):
        pixel_center = Ray_tracer_main.pixel100_loc + (i * Ray_tracer_main.pixel_delta_u) \
                       + (j * Ray_tracer_main.pixel_delta_v)
        ray_direction = pixel_center - Ray_tracer_main.camera_center
        r = ray.Ray(Ray_tracer_main.camera_center, ray_direction)

        pixel_color = Color_Utils.color(Color_Utils.ray_color(r))
        row.append(Color_Utils.write_color(pixel_color))
    print("row")
    print(len(row))
    rgb_values.append(row)

# Ici, il faudra simplement mettre l'array finit du raytracing pour que tkinter l'affiche
print(len(rgb_values))
Tkinter_Output.output(rgb_values, int(width), int(height))
