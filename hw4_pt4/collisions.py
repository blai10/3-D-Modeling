import math
import vector_math
import data


def sphere_intersection_point(ray, sphere):
    diff_ray_to_sphere = vector_math.difference_vector(ray.pt, sphere.center)
    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = 2 * vector_math.dot_vector(diff_ray_to_sphere, ray.dir)
    c = vector_math.dot_vector(diff_ray_to_sphere, diff_ray_to_sphere) - sphere.radius * sphere.radius

    discriminant = (b * b) - (4 * (a * c))
    if discriminant < 0:
        return None
    t1 = (((-1 * b) + math.sqrt(discriminant)) / (2 * a))
    t2 = (((-1 * b) - math.sqrt(discriminant)) / (2 * a))
    if t1 >= 0 and t2 < 0:
        return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, t1)))
    elif t1 < 0 and t2 >= 0:
        return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, t2)))
    elif t1 >= 0 and t2 >= 0:
        if t1 < t2:
            return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, t1)))
        else:
            return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, t2)))
    else:
        return None


def find_intersection_points(sphere_list, ray):
    intersection_list = []
    for i in sphere_list:
        intersect = sphere_intersection_point(ray, i)
        if intersect is not None:
            intersection_list.append((i, intersect))
    return intersection_list


def sphere_normal_at_point(sphere, point):
    return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
