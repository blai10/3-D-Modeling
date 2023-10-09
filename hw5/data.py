import utility


class point:

    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

    def __eq__(self, other):
        x = utility.epsilon_equal(self.x, other.x)
        y = utility.epsilon_equal(self.y, other.y)
        z = utility.epsilon_equal(self.z, other.z)
        return x and y and z




class vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        x1 = utility.epsilon_equal(self.x, other.x)
        y1 = utility.epsilon_equal(self.y, other.y)
        z1 = utility.epsilon_equal(self.z, other.z)
        return x1 and y1 and z1



class ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        pt1 = point.__eq__(self.pt, other.pt)
        dir1 = vector.__eq__(self.dir, other.dir)
        return pt1 and dir1


class sphere:
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        center1 = point.__eq__(self.center, other.center)
        radius1 = utility.epsilon_equal(self.radius, other.radius)
        color1 = utility.epsilon_equal(self.color, other.color)
        finish1 = utility.epsilon_equal(self.finish, other.finish)
        return center1 and radius1 and color1 and finish1

class color:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    def __eq__(self, other):
        return utility.epsilon_equal(self.r, other.r) and utility.epsilon_equal(self.g, other.g) and utility.epsilon_equal(self.b, other.b)

class finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.amb = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        ambient1 = utility.epsilon_equal(self.amb, other.amb)
        diffuse1 = utility.epsilon_equal(self.diffuse, other.diffuse)
        specular1 = utility.epsilon_equal(self.specular, other.specular)
        roughness1 = utility.epsilon_equal(self.roughness, other.roughness)
        return ambient1 and diffuse1 and specular1 and roughness1

class light:
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        pt1 = utility.epsilon_equal(self.pt, other.pt)
        color1 = utility.epsilon_equal(self.color, other.color)
        return pt1 and color1

