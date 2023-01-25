import unittest
from Vector3 import Vector3
import numpy as np


class TestVector3(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector3(1, 2, 3)
        self.v2 = Vector3(4, 5, 6)
        self.v3 = Vector3(0, 0, 0)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vector3(5, 7, 9))

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vector3(-3, -3, -3))

    def test_mul(self):
        self.assertEqual(3 * self.v1, Vector3(3, 6, 9))
        self.assertEqual(self.v1 * 3, Vector3(3, 6, 9))

    def test_div(self):
        self.assertEqual(self.v2 / 2, Vector3(2, 2.5, 3))

    def test_str(self):
        self.assertEqual(str(self.v1), f"({1}, {2}, {3})")

    def test_repr(self):
        self.assertEqual(repr(self.v1), f"Vector3({1}, {2}, {3})")

    def test_relational_operators(self):
        self.assertEqual(self.v1 == self.v1, True)
        self.assertEqual(self.v1 == self.v2, False)
        self.assertEqual(self.v1 != self.v2, True)

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), 32)
        self.assertEqual(self.v1.dot(self.v3), 0)

    def test_norm(self):
        self.assertEqual(self.v1.norm(), np.sqrt(14))
        self.assertEqual(self.v3.norm(), 0)

    def test_normalize(self):
        self.assertEqual(self.v1.normalize(), self.v1 / self.v1.norm())

    def test_components(self):
        self.assertEqual(self.v1.components(), (1, 2, 3))


if __name__ == '__main__':
    unittest.main()
