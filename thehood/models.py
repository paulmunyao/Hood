from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Neighbourhood(models.Model):
    image = CloudinaryField('image', default='True')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def find_neighbourhood(self):
        return Neighbourhood.objects.filter(id=self.id)

    def update_neighbourhood(self):
        self.update()

    def update_occupants(self):
        self.occupants += 1

    def delete_occupants(self):
        self.occupants -= 1

    def __str__(self):
        return f'{self.name}'


class Business(models.Model):
    image = CloudinaryField('image', default='True')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self):
        return Business.objects.filter(id=self.id)

    def update_business(self):
        self.update()

    def __str__(self):
        return f'{self.name} Business'
