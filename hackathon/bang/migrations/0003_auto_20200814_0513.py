# Generated by Django 2.1.1 on 2020-08-14 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0002_bang_posision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bang',
            old_name='image',
            new_name='images',
        ),
    ]
