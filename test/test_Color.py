import unittest
from Color import Color


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.blue = Color.from_hex("#0000FF")
        self.cyan = Color.from_hex("#00FFFF")
        self.red = Color.from_hex("#FF0000")
        self.pink = Color.from_hex("#C4368F")

    def test_from_hex(self):
        self.assertEqual(self.blue.components(), (0, 0, 1))
        self.assertEqual(self.cyan.components(), (0, 1, 1))
        self.assertEqual(self.red.components(), (1, 0, 0))
        self.assertEqual(self.pink.components(), (196/255, 54/255, 143/255))


if __name__ == '__main__':
    unittest.main()
