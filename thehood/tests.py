from django.test import TestCase
from .models import Business, Profile, Neighbourhood, User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test')
        self.profile = Profile.objects.create(user=self.user, bio='test bio', location='test location', description='test description')

    def test_profile_content(self):
        self.assertEqual(f'{self.user.username} Profile', str(self.profile))
        self.assertEqual(self.profile.image,'test image')
        self.assertEqual(self.profile.bio, 'test bio')
        self.assertEqual(self.profile.location, 'test location')
        self.assertEqual(self.profile.description, 'test description')

            

class BusinessTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.business = Business.objects.create(name='test', id='1', email='test')

    def test_business_content(self):
        self.assertEqual(f'{self.business.name}', 'test')
        self.assertEqual(f'{self.business.id}', '1')
        self.assertEqual(f'{self.business.neighbourhood}', 'test')
        self.assertEqual(f'{self.business.email}', 'test')

