import unittest
from app import create_app

class ChatbotTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Personalized Quote Generator', response.data)

    def test_generate_quote(self):
        response = self.client.post('/', data={'problem': 'I am feeling sad'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your Quote:', response.data)

if __name__ == '__main__':
    unittest.main()
