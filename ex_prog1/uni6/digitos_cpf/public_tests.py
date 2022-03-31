import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global calcula_digitos_verificacao
        undertest = __import__(module)
        calcula_digitos_verificacao = getattr(undertest, 'calcula_digitos_verificacao', None)

    def test_basico(self):
        assert calcula_digitos_verificacao('153245875') == '40'


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
