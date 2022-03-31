import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global maior_slice
        undertest = __import__(module)
        maior_slice = getattr(undertest, 'maior_slice', None)

    def test_1_publico(self):
        assert maior_slice([1, 2, 3, 4, 2, 0, 1]) == [1, 2, 3, 4]
        assert maior_slice([7, 6, 2, 9, 10]) == [2, 9, 10]
        assert maior_slice([7, 8, 9, 1, 2, 3, 0]) == [1, 2, 3]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
