import unittest
from app import construct_query

class TestQueryConstruction(unittest.TestCase):
    def test_linkedin_query(self):
        query = construct_query("LinkedIn", "Udaipur")
        expected = 'site:linkedin.com/in ("Principal" OR "Director") "Udaipur" "admissions"'
        self.assertEqual(query, expected)

    def test_facebook_query(self):
        query = construct_query("Facebook", "Jhansi", "hiring")
        expected = 'site:facebook.com ("Principal" OR "Director") "Jhansi" "hiring"'
        self.assertEqual(query, expected)

    def test_instagram_query(self):
        query = construct_query("Instagram", "Madurai")
        expected = 'site:instagram.com ("Principal" OR "Director") "Madurai" "admissions"'
        self.assertEqual(query, expected)

if __name__ == '__main__':
    unittest.main()
