import unittest
from app import sumar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()


class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        from app import multiplicar
        self.assertEqual(multiplicar(2, 3), 6)
