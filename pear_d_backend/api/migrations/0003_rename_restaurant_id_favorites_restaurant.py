# Generated by Django 4.1.3 on 2022-12-06 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_favorites_restaurant_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorites',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
    ]
