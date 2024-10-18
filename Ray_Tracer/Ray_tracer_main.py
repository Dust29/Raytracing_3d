from Ray_Tracer import Vec3_Class


def hit_sphere(center, radius, r):
    oc = r.origin() + center
    a = Vec3_Class.dot(r.direction(), r.direction())
    b = -2.0 * Vec3_Class.dot(r.direction(), oc)
    c = Vec3_Class.dot(oc,oc) - radius*radius
    discriminant = b*b - 4*a*c
    return discriminant >= 0

aspect_ratio = 16.0/9.0
width = 400

# On calcule la hauteur de l'image, et on s'assure qu'elle soit au moins de 1
height = width/aspect_ratio
height = 1 if height < 1 else height

# Paramètres de la caméra (Non, vraiment)
focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (width/height)
camera_center = Vec3_Class.Vec3(0, 0, 0)

# Calcul des vecteurs pour le viewports (?) (Voir le tuto)
viewport_u = Vec3_Class.Vec3(viewport_width, 0, 0)
viewport_v = Vec3_Class.Vec3(0, -viewport_height, 0)

# Calcul des deltas de pixel a pixel (Pour faire la trad entre les coordonées image et caméra ? (Idk, voir le tuto)
pixel_delta_u = viewport_u / width
pixel_delta_v = viewport_v / height

# Calcul de la localisation du pixel en haut à gauche
viewport_upper_left = camera_center - Vec3_Class.Vec3(0,0, focal_length) - viewport_u / 2 - viewport_v / 2
pixel100_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

