from django.test import TestCase


# Create your tests here.
class AccountTest(TestCase):
    
    def test_pseudo(self):
        a = 'login'
        b = 'login'
        self.assertEqual(a,b)