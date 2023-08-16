import requests
import unittest
import collections
collections.Callable = collections.abc.Callable


class TestWebsiteLoading(unittest.TestCase):
    def test_website_loading(self):
        url = 'https://atg.world'
        response = requests.get(url)
        
        # Print status code for debugging purposes
        print(f"Status code: {response.status_code}")
        
        # Check if the website loaded successfully
        self.assertEqual(response.status_code, 200, "Website did not load properly")

if __name__ == '__main__':
    unittest.main()

