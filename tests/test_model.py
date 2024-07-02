import unittest
from app.model import generate_quote

class ModelTestCase(unittest.TestCase):

    def test_generate_quote(self):
        problem = "I am feeling sad"
        quote = generate_quote(problem)
        self.assertTrue(isinstance(quote, str))
        self.assertGreater(len(quote), 0)

if __name__ == '__main__':
    unittest.main()
