import collisions
import data
import vector_math


def cast_ray(ray, sphere_list):
    if collisions.find_intersection_points(sphere_list, ray):
        return True
    else:
        return False


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height

    image = open('image.ppm', 'w')
    image.write('P3\n')
    image.write(f'{width} {height}\n')
    image.write('255\n')

    for e in range(height):
        for i in range(width):
            x = min_x + (i * step_x)
            y = max_y - (e * step_y)
            pt = data.point(x, y, 0)
            ray = data.ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            intersections = cast_ray(ray, sphere_list)
            if intersections:
                image.write('0 0 0\n')
            else:
                image.write('255 255 255\n')
    image.close()
