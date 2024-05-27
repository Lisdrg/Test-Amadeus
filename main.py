import unittest
import requests

class AmadeusTestChallenge(unittest.TestCase):
    
    def setUp(self):
        #ARRANGE
        self.url='https://api.restful-api.dev/objects'
        self.expected_keys=['id','name','data']
        
    def test_validate_response_success(self):   
        #ARRANGE
        self.expected_status_code = 200
        
        #ACT
        response = requests.get(self.url)
        devices = response.json()
        
        #ASSERT
        self.assertEqual(response.status_code,self.expected_status_code, 'Expected status code: 200')

        for device in devices:
            for expected_key in self.expected_keys:
                self.assertIn(expected_key, device, f"Missing expected key '{expected_key}' in response")
                
    def test_validate_response_not_found(self):
        #ARRANGE
        self.modified_url= self.url + 'invalid'
        self.expected_status_code = 404
        
        #ACT
        response = requests.get(self.modified_url)
        
        #ASSERT
        self.assertEqual(response.status_code,self.expected_status_code, 'Expected status code: 404')
           
    
if __name__ == '__main__':
    unittest.main()
    
