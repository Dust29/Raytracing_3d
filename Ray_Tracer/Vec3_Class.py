import math


# Ici, on crée une classe vec3, qui nous servira pour plein de choses différentes.
class Vec3:
    def __init__(self, e0=0.0, e1=0.0, e2=0.0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value


    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self


    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])
        elif isinstance(other, (int, float)):  # Si other est un scalaire
            return Vec3(self.e[0] + other, self.e[1] + other, self.e[2] + other)
        else:
            raise TypeError("Addition not supported between instances of 'Vec3' and other types")


    def __sub__(self, other):
        return Vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])


    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __mul__(self, t):
        if isinstance(t, (int, float)):  # Si t est un scalaire
            return Vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)
        elif isinstance(t, Vec3):  # Si t est un autre vecteur, on fait la multiplication terme à terme
            return Vec3(self.e[0] * t.e[0], self.e[1] * t.e[1], self.e[2] * t.e[2])
        else:
            raise TypeError("Multiplication not supported between instances of 'Vec3' and other types")


    def __rmul__(self, t):
        # Appelle simplement __mul__ avec les arguments inversés
        return self.__mul__(t)


    def __itruediv__(self, t):
        return self.__imul__(1 / t)


    def __truediv__(self, t):
        if t != 0:  # On vérifie pour éviter la division par zéro
            return Vec3(self.e[0] / t, self.e[1] / t, self.e[2] / t)
        else:
            raise ValueError("Division par zéro impossible.")


    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2

    def __repr__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"


# Alias for Vec3 for geometric clarity
Point3 = Vec3

# Vector Utility Functions


def dot(u, v):
    return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]


def cross(u, v):
    return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                u.e[2] * v.e[0] - u.e[0] * v.e[2],
                u.e[0] * v.e[1] - u.e[1] * v.e[0])


def unit_vector(v):
    return v / v.length()


def operator_add(u, v):
    return Vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2])


def operator_sub(u, v):
    return Vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2])


def operator_mul_vec(u, v):
    return Vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2])


def operator_mul_scalar(t, v):
    return Vec3(t * v.e[0], t * v.e[1], t * v.e[2])


def operator_div(v, t):
    return Vec3(v.e[0] / t, v.e[1] / t, v.e[2] / t)
