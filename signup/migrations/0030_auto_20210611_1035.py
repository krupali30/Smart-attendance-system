# Generated by Django 3.2.3 on 2021-06-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0029_profile_abnormal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='abnormal',
            field=models.BooleanField(default='No'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='attendance',
            field=models.BooleanField(default='Absent'),
        ),
    ]
