import stock
import unittest

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('ibm',100,3.2)
        self.assertEqual(s.name,'ibm')
        self.assertEqual(s.shares,100)
        self.assertEqual(s.price,3.2)
    
    def test_cost(self):
        s = stock.Stock('intel',200,3.1)
        c = s.cost
        self.assertEqual(c,620)
    
    def test_sell(self):
        s = stock.Stock('intel',200,3.1)
        s.sell(20)
        self.assertEqual(s.shares,180)

    def test_type_shares(self):
        s = stock.Stock('intel',200,3.1)
        with self.assertRaises(TypeError):
            s.shares = '200'

if __name__ == '__main__':
    unittest.main()