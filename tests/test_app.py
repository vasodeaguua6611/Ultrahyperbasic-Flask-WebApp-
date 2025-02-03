
import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_hello(self):
        result = self.app.get('/hello/John/')
        self.assertEqual(result.status_code, 200)

    def test_members(self):
        result = self.app.get('/members')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()