import simple
import unittest

class TestAdd(unittest.TestCase):
    def test_simple(self):
        r = simple.add(2,3)
        self.assertEqual(r,4)
    def test_str(self):
        r = simple.add('hello','world')
        self.assertEqual(r,'hello world')

    
if __name__ == '__main__':
    unittest.main()