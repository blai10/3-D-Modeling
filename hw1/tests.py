import unittest
import data


class TestCases(unittest.TestCase):
    def test_point(self):
        p = data.point(1, 2, 3)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3)

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

    if __name__ == '__main__':
        unittest.main()
