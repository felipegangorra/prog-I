import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class AcceptanceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global idosos_inicio
        undertest = __import__(module)
        idosos_inicio = getattr(undertest, 'idosos_inicio', None)

    def test_exemplo(self):
        fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
        self.assertEqual( idosos_inicio(fila), None )
        self.assertEqual( fila, [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34])

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
