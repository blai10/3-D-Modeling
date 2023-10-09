import unittest
import data
import utility
import vector_math


class TestCases(unittest.TestCase):
    def test_point(self):
        p = data.point(1, 2, 3)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3)
        self.assertTrue(utility.epsilon_equal(p.x, 1))
        self.assertFalse(utility.epsilon_equal(p.x, 2))

    def test_vector(self):
        v = data.vector(1.0, 0.0, 0.0)
        self.assertEqual(v.x, 1.0)
        self.assertEqual(v.y, 0.0)
        self.assertEqual(v.z, 0.0)

    def test_ray(self):
        pt = data.point(1, 2, 3)
        dir = data.vector(1.0, 0.0, 0.0)
        ray = data.ray(pt, dir)
        self.assertEqual(ray.pt.x, 1)
        self.assertEqual(ray.pt.y, 2)
        self.assertEqual(ray.pt.z, 3)
        self.assertEqual(ray.dir.x, 1.0)
        self.assertEqual(ray.dir.y, 0.0)
        self.assertEqual(ray.dir.z, 0.0)

    def test_sphere(self):
        pt = data.point(1, 2, 3)
        sphere = data.sphere(pt, 2.0)
        self.assertEqual(sphere.center.x, 1)
        self.assertEqual(sphere.center.y, 2)
        self.assertEqual(sphere.center.z, 3)
        self.assertEqual(sphere.radius, 2.0)

    def test_scale_vector(self):
        v = data.vector(1, 2, 3)
        scale_vector = vector_math.scale_vector(v, 1.5)
        self.assertEqual(scale_vector.x, 1.5)
        self.assertEqual(scale_vector.y, 3)
        self.assertEqual(scale_vector.z, 4.5)

    def test_dot_vector(self):
        v1 = data.vector(1, 2, 3)
        v2 = data.vector(5, 4, 6)
        self.assertEqual(vector_math.dot_vector(v1, v2), 31)

    def test_length_vector(self):
        v = data.vector(3, 1, 2)
        self.assertAlmostEqual(vector_math.length_vector(v), 3.74, 2)

    def test_normalize_vector(self):
        v = data.vector(3, 1, 2)
        vector = vector_math.normalize_vector(v)
        self.assertAlmostEqual(vector.x, 0.80, 2)
        self.assertAlmostEqual(vector.y, 0.27, 2)
        self.assertAlmostEqual(vector.z, 0.53, 2)

    def test_difference_point(self):
        pt1 = data.point(4, 7, 9)
        pt2 = data.point(1, 2, 3)
        point = vector_math.difference_point(pt1, pt2)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 5)
        self.assertEqual(point.z, 6)

    def test_difference_vector(self):
        v1 = data.vector(1.0, 2.0, 3.0)
        v2 = data.vector(0.5, 1.2, 2.7)
        vector = vector_math.difference_vector(v1, v2)
        self.assertAlmostEqual(vector.x, 0.5)
        self.assertAlmostEqual(vector.y, 0.8)
        self.assertAlmostEqual(vector.z, 0.3)

    def test_translate_point(self):
        pt = data.point(9, 0, 1)
        v = data.vector(1, 2, 3)
        point = vector_math.translate_point(pt, v)
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.z, 4)

    def test_vector_from_to(self):
        to_point = data.point(10, 2, 4)
        from_point = data.point(1, 2, 3)
        vector = vector_math.vector_from_to(from_point, to_point)
        self.assertEqual(vector.x, 9)
        self.assertEqual(vector.y, 0)
        self.assertEqual(vector.z, 1)

    if __name__ == '__main__':
        unittest.main()
