import unittest
from run import app

class BaseTestCase(unittest.TestCase):
    "This is the parent class "
    def setUp(self):
        """
        This method runs before each test
        """
        self.app = app.test_client(self) #gives the test client of the app