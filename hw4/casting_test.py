import cast
import data
import unittest


sphere_list = [data.sphere(data.point(1.0, 1.0, 0.0), 2), data.sphere(data.point(0.5, 1.5, -3.0), 0.5)]
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.point(0.0, 0.0, -14.0), sphere_list)
