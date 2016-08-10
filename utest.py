import os
import unittest



class myclass():
    def cube(self, n):
        return n**3

    def triarea(self, base,height):
        return base* height / 2




class MyTest(unittest.TestCase):
    def test_o(self):
        self.assertEqual(myclass.cube(myclass, 5), 125)
        self.assertEqual(myclass.cube(myclass, 10), 1000)
        self.assertEqual(myclass.cube(myclass,0), 0)


if __name__ == "__main__":
    unittest.main()


