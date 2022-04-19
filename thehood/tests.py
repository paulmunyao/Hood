from django.test import TestCase
from .models import Business, Profile, Neighbourhood, User

# Create your tests here.


class BusinessTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.business = Business.objects.create(name='test', id='1', email='test')

    def test_business_content(self):
        self.assertEqual(f'{self.business.name}', 'test')
        self.assertEqual(f'{self.business.id}', '1')
        self.assertEqual(f'{self.business.neighbourhood}', 'test')
        self.assertEqual(f'{self.business.email}', 'test')
