# Generated by Django 4.1.1 on 2024-03-19 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0005_rename_category_pet_product_categoryy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet_product',
            old_name='categoryy',
            new_name='category',
        ),
    ]
