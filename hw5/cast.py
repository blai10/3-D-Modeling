import time

import collisions
import data
import vector_math
import math


def convert_to_int(number):
    num = int(number * 22)
    if num > 255:
        return 255
    else:
        return num


def get_distance(point1, point2):
    distance = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2 + (point2.z - point1.z) ** 2)
    return distance


def cast_ray(ray, sphere_list, ambient_color, light, point):
    collisions_list = collisions.find_intersection_points(sphere_list, ray)
    if collisions_list:
        smallest_length = vector_math.length_vector(vector_math.difference_vector(collisions_list[0][1], ray.pt))
        sphere = collisions_list[0][0]
        smallest_num = 0
        for i in range(len(collisions_list)):
            if vector_math.length_vector(
                    vector_math.difference_vector(collisions_list[i][1], ray.pt)) < smallest_length:
                smallest_num = i
                smallest_length = vector_math.length_vector(
                    vector_math.difference_vector(collisions_list[i][1], ray.pt))
                sphere = collisions_list[i][0]
        normal = collisions.sphere_normal_at_point(collisions_list[smallest_num][0],
                                                   collisions_list[smallest_num][1])
        scalar = vector_math.scale_vector(normal, .01)
        pe = vector_math.translate_point(collisions_list[smallest_num][1], scalar)
        light_direction = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))
        dot_vector1 = vector_math.dot_vector(normal, light_direction)
        reflect_vector = vector_math.difference_vector(light_direction,
                                                       vector_math.scale_vector(normal, (2 * dot_vector1)))
        vector_direction = vector_math.normalize_vector(vector_math.vector_from_to(point, pe))
        specular = vector_math.dot_vector(reflect_vector, vector_direction)
        r = 0
        g = 0
        b = 0
        if dot_vector1 > 0:
            pe_ray = data.ray(pe, light_direction)
            ray_intersections = collisions.find_intersection_points(sphere_list, pe_ray)
            if not ray_intersections:
                r = r + dot_vector1 * light.color.r * sphere.color.r * ambient_color.r * sphere.finish.diffuse
                g = g + dot_vector1 * light.color.g * sphere.color.g * ambient_color.g * sphere.finish.diffuse
                b = b + dot_vector1 * light.color.b * sphere.color.b * ambient_color.b * sphere.finish.diffuse

                if specular > 0:
                    r = r + light.color.r * sphere.finish.specular * (specular ** (1.0 / sphere.finish.roughness))
                    g = g + light.color.g * sphere.finish.specular * (specular ** (1.0 / sphere.finish.roughness))
                    b = b + light.color.b * sphere.finish.specular * (specular ** (1.0 / sphere.finish.roughness))
        r = r + sphere.color.r * ambient_color.r * sphere.finish.amb
        g = g + sphere.color.g * ambient_color.g * sphere.finish.amb
        b = b + sphere.color.b * ambient_color.b * sphere.finish.amb
        if r > 1:
            r = 1
        if g > 1:
            g = 1
        if b > 1:
            b = 1

        return data.color(r, g, b)
    else:
        return data.color(1, 1, 1)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, finish, light):
    start = time.time()
    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height
    output_file = open("image.ppm", "w")
    output_file.write("P3\n")
    output_file.write(str(width) + " " + str(height) + "\n")
    output_file.write("255\n")

    for e in range(height):
        print('Casting Ray', e + 1, 'of', height, 'Time Elapsed:',
              time.strftime('%H:%M:%S', time.gmtime(time.time() - start)), end='\r')
        for i in range(width):
            x = min_x + (i * step_x)
            y = max_y - (e * step_y)
            pt = data.point(x, y, 0)
            ray = data.ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            intersections = cast_ray(ray, sphere_list, finish, light, eye_point)
            output_file.write(f'{int(intersections.r * 255)} {int(intersections.g * 255)} {int(intersections.b * 255)}\n')
