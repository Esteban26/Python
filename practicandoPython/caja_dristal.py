import unittest

def es_mayor_edad(edad):
    if edad > 18:
        return True
    else:
        return False


class PruebasDeCristalTest(unittest.TestCase):
    
    def es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_edad(edad)

        self.resultado = True

    def es_menor_de_edad(self):
        edad = 10

        resultado = es_mayor_edad(edad)

        self.resultado = True

if __name__ == '__main__':
    unittest.main()