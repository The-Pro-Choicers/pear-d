# Generated by Django 4.1.3 on 2022-11-21 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Profile',
            new_name='UserProfile',
        ),
    ]
