# Generated by Django 3.2 on 2021-05-26 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storemaster', '0007_auto_20210525_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webstore',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='webstore',
            name='modified_date',
        ),
    ]