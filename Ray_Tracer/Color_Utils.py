from Ray_Tracer import Vec3_Class,Ray_tracer_main

def color(e):
    return Vec3_Class.Vec3(e[0], e[1], e[2])


# Dans cette fonction, on prend un pixel et on en extrait les couleurs
def write_color(pixel_color):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # On traduit de l'intervalle [0,1] a l'intervalle [0,255]
    rbyte = int(255.999*r)
    gbyte = int(255.999*g)
    bbyte = int(255.999*b)

    # Afficher la couleur du pixel
    #print(f"{rbyte} {gbyte} {bbyte}")

    return [rbyte, gbyte, bbyte]

def ray_color(r):
    if Ray_tracer_main.hit_sphere(Vec3_Class.Point3(0,0,-1), 0.5 , r):
        return color([1,0,0])
    unit_direction = Vec3_Class.unit_vector(r.direction())
    a = 0.5 * (1.0-unit_direction.x()) #x instead of y here, idk why
    return (1.0-a)* color([1.0,1.0,1.0]) + a * color([0.5,0.7,1.0])