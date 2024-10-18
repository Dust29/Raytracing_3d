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

    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t):
        return self.__imul__(1 / t)

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
