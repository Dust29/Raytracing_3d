from Ray_Tracer import Vec3_Class

color = Vec3_Class.Vec3


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
    print(f"{rbyte} {gbyte} {bbyte}")

    return [rbyte, gbyte,bbyte]