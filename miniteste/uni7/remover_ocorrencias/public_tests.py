import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_ocorrencias
        undertest = __import__(module)
        remove_ocorrencias = getattr(undertest, 'remove_ocorrencias', None)

    def test_example(self):
        lista = [1, "Prog1", 3.4, 1]
        assert remove_ocorrencias(lista, 1) == 1
        assert lista == ["Prog1", 3.4]

    def test_exemplo2(self):
        lista = [1, "Prog1", 3.4, 1]
        assert remove_ocorrencias(lista, 2) == None
        assert lista == [1, "Prog1", 3.4, 1]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
