# Generated by Django 3.2.3 on 2021-06-08 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0016_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
    ]
