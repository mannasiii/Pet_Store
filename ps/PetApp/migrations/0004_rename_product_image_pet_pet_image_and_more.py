# Generated by Django 4.1.1 on 2024-03-19 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0003_pet_delete_pets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='product_image',
            new_name='pet_image',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='product_title',
            new_name='pet_title',
        ),
    ]
