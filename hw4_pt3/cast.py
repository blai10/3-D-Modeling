import collisions
import data
import vector_math
import math

def get_distance(point1, point2):
    distance = math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2 + (point2.z - point1.z) ** 2)
    return distance

def calculate_color(color):
    r = int(color.r * 255)
    g = int(color.g * 255)
    b = int(color.b * 255)
    return data.color(r, g, b)


def cast_ray(ray, sphere_list, ambient_color):
    color = data.color(1, 1, 1)
    smallest_length = math.inf
    if collisions.find_intersection_points(sphere_list, ray):
        for i in collisions.find_intersection_points(sphere_list, ray):
            length = get_distance(i[1], ray.pt)
            if length < smallest_length:
                smallest_length = length
                color = i[0].color
                finish = i[0].finish.amb
                r = color.r * finish * ambient_color.r
                g = color.g * finish * ambient_color.g
                b = color.b * finish * ambient_color.b
                color = data.color(r, g, b)
    return color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, finish):
    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height

    print('P3')
    print(width, height)
    print('255')

    for e in range(height):
        for i in range(width):
            x = min_x + (i * step_x)
            y = max_y - (e * step_y)
            pt = data.point(x, y, 0)
            ray = data.ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            intersections = cast_ray(ray, sphere_list, finish)
            print(f'{int(intersections.r * 255)} {int(intersections.g * 255)} {int(intersections.b * 255)}')

# def calculate_color(color):
#    r = int(color.r * 255)
#    g = int(color.g * 255)
#   b = int(color.b * 255)
#    return data.color(r, g, b)


# def cast_ray(ray, sphere_list):
#    if collisions.find_intersection_points(sphere_list, ray):
#        closest_length = math.inf
#        for e in collisions.find_intersection_points(sphere_list, ray):
#            length = vector_math.length_vector(vector_math.difference_vector(ray.pt, e[1]))
#            if length <= closest_length:
#                color1 = e[0].color
#                closest_length = length
#        return calculate_color(color1)
#    else:
#        return data.color(255, 255, 255)
