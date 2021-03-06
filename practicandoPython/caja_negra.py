import unittest
from unittest import result

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 50

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def suma_dos_Negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)    


if __name__ == '__name__':
    unittest.main()