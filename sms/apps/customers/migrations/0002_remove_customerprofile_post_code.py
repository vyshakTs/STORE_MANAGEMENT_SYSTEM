# Generated by Django 3.2 on 2021-05-23 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='post_code',
        ),
    ]
