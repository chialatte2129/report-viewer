# Generated by Django 4.1.1 on 2022-10-08 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_doors_is_car_park'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doors',
            new_name='Door',
        ),
    ]
