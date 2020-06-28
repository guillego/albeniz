
import albeniz
import unittest


class BasicTestCase(unittest.TestCase):
    """ Basic test cases """

    def test_basic(self):
        """ check True is True """
        self.assertTrue(True)

    def test_version(self):
        """ check albeniz exposes a version attribute """
        self.assertTrue(hasattr(albeniz, "__version__"))
        self.assertIsInstance(albeniz.__version__, str)


if __name__ == "__main__":
    unittest.main()
