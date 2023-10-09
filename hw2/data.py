import utility


class point:

    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) or utility.epsilon_equal(self.y,
                                                                               other.y) or utility.epsilon_equal(self.z,
                                                                                                                 other.z)






class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) or utility.epsilon_equal(self.y,
                                                                               other.y) or utility.epsilon_equal(self.z,
                                                                                                                 other.z)


class ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) or utility.epsilon_equal(self.dir, other.dir)


class sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return utility.epsilon_equal(self.center, other.center) or utility.epsilon_equal(self.radius, other.radius)

