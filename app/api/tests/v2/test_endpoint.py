import unittest

from app import appCreate

class TestEndpoints(unittest.TestCase):

    def setup(self):
        ''' create instance of the app for testing '''
        self.app = appCreate()
        self.client = self.app.test_client()
        
    def test_getredflags(self):
        ''' Test the Redflags endpoint ''' 
        self.app = appCreate()
        self.client = self.app.test_client
        response = self.client().get('/api/v2/Redflags')
        self.assertEqual(response.status_code, 404)
        