import unittest
import sys

module  = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global organiza_pedido
        undertest = __import__(module)
        organiza_pedido = getattr(undertest, 'organiza_pedido', None)

    def test_basico(self):
        l = ['s', 'd', 'd', 'p', 's', 'd', 's']
        assert organiza_pedido(l) == None
        assert l == ['d', 'd', 'd', 'p', 's', 's', 's']


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
