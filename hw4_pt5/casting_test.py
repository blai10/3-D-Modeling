import cast
import data
import unittest


eye_point = data.point(0.0, 0.0, -14.0)
light = data.light(data.point(-100, 100, -100), data.color(1.5, 1.5, 1.5))
small_sphere = data.sphere(data.point(0.5, 1.5, -3.0), 0.5, data.color(1, 0, 0), data.finish(0.4, 0.4, 0.5, .05))
big_sphere = data.sphere(data.point(1.0, 1.0, 0.0), 2, data.color(0, 0, 1), data.finish(0.2, 0.4, 0.5, .05))
sphere_list = [big_sphere, small_sphere]
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, eye_point, sphere_list, data.color(1.0, 1.0, 1.0), light)






