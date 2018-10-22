import unittest
from run import app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """
        This method executes before each test run
        """
        self.app = app.test_client(self)