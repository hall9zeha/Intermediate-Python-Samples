import unittest
def doblar(a): return a*2
def sumar(a,b): return a+b
def es_par(a): return True if a%2==0 else False
class Pruebas(unittest.TestCase):

    def test(self):

        raise AssertionError()
    def test1(self):

        1/0
    def test_doblar(self):
        self.assertEqual(doblar(10),20)
        self.assertEqual(doblar('Ab'),'AbAb')
    def test_sumar(self):
        self.assertEqual(sumar(-15,15),0)
        self.assertEqual(sumar('Ab','cd'),'Abcd')
    def test_espar(self):
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)
class PruebaMetodosYCadenas(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hola'.upper(),'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('hola'.isupper())
    def test_split(self):
        s="Hola mundo"
        self.assertEquals(s.split(" "), ['Hola','mundo'])
if __name__ == "__main__":
    unittest.main()