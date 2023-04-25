import unittest

from decimal_binario import decimal_binario

class TestNumeracion(unittest.TestCase):
      
    

     def test_decimal2binario(self):
          self.assertEqual(decimal_binario(97,"01100001"))
     
     def test_decimal2binario(self):
          self.assertEqual(decimal_binario(51,"110011"))

     def test_decimal2binario(self):
          self.assertEqual(decimal_binario(42,"101010"))
     

          

          
if __name__== '__main__':
    unittest.main()