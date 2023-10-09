class point:
    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir


class sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
