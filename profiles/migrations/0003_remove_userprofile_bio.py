# Generated by Django 3.2.16 on 2022-11-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_profile_picture_userprofile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
    ]
