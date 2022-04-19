# Generated by Django 4.0.4 on 2022-04-19 10:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thehood', '0008_remove_business_image_remove_neighbourhood_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=cloudinary.models.CloudinaryField(default='True', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=cloudinary.models.CloudinaryField(default='True', max_length=255, verbose_name='image'),
        ),
    ]
