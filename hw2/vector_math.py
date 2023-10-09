import math


def scale_vector(vector, scalar):
    vector.x = vector.x * scalar
    vector.y = vector.y * scalar
    vector.z = vector.z * scalar
    return vector


def dot_vector(vector1, vector2):
    vector_x = (vector1.x * vector2.x)
    vector_y = (vector1.y * vector2.y)
    vector_z = (vector1.z * vector2.z)
    answer_dot_vector = (vector_x + vector_y + vector_z)
    return answer_dot_vector


def length_vector(vector):
    def sqr(x):
        return x * x

    vector = math.sqrt((sqr(vector.x)) + (sqr(vector.y)) + (sqr(vector.z)))
    return vector


def normalize_vector(vector):
    def sqr(x):
        return x * x

    length_vector = math.sqrt((sqr(vector.x)) + (sqr(vector.y)) + (sqr(vector.z)))
    vector.x = (vector.x / length_vector)
    vector.y = (vector.y / length_vector)
    vector.z = (vector.z / length_vector)
    return vector


def difference_point(point1, point2):
    point1.x = (point1.x - point2.x)
    point1.y = (point1.y - point2.y)
    point1.z = (point1.z - point2.z)
    return point1


def difference_vector(vector1, vector2):
    vector1.x = (vector1.x - vector2.x)
    vector1.y = (vector1.y - vector2.y)
    vector1.z = (vector1.z - vector2.z)
    return vector1


def translate_point(point, vector):
    point.x = (point.x + vector.x)
    point.y = (point.y + vector.y)
    point.z = (point.z + vector.z)
    return point


def vector_from_to(from_point, to_point):
    to_point.x = (to_point.x - from_point.x)
    to_point.y = (to_point.y - from_point.y)
    to_point.z = (to_point.z - from_point.z)
    return to_point
