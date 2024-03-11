import unittest
from email_source import CSVEmailSource

class TestIsNewsletter(unittest.TestCase):
    def test_is_newsletter(self):
        with open('minimi Coding Test - Dataset - email_dataset.csv', 'r') as csv_file:
            email_source = CSVEmailSource(csv_file)
        
            self.assertTrue(email_source.is_newsletter("Please unsubscribe me from this list."))
            self.assertTrue(email_source.is_newsletter("How do I subscribe to your newsletter?"))
            self.assertFalse(email_source.is_newsletter("Hello, how are you?"))

if __name__ == '__main__':
    unittest.main()
