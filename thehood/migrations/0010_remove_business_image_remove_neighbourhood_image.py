# Generated by Django 4.0.4 on 2022-04-19 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thehood', '0009_business_image_neighbourhood_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='image',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='image',
        ),
    ]
