from Ray_Tracer import Vec3_Class


class Ray:
    def __init__(self, origin=None, direction=None):
        # Si aucun argument n'est donné, on initialise les attributs avec des valeurs par défaut (None)
        self.orig = origin if origin is not None else Vec3_Class.Vec3(0, 0, 0)
        self.dir = direction if direction is not None else Vec3_Class.Vec3(0, 0, 0)

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t):
        # Retourne le point à une distance t le long du rayon
        return self.orig + self.dir * t