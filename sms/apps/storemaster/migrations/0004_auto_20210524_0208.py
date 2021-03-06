# Generated by Django 3.2 on 2021-05-23 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_post_code_postcode_pin_code'),
        ('storemaster', '0003_webstore_post_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webstore',
            old_name='current_address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='webstore',
            old_name='permanent_address',
            new_name='address2',
        ),
        migrations.RenameField(
            model_name='webstore',
            old_name='name',
            new_name='store_name',
        ),
        migrations.RemoveField(
            model_name='webstore',
            name='language',
        ),
        migrations.RemoveField(
            model_name='webstore',
            name='url',
        ),
        migrations.RemoveField(
            model_name='webstore',
            name='country',
        ),
        migrations.AddField(
            model_name='webstore',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.country'),
        ),
        migrations.RemoveField(
            model_name='webstore',
            name='state',
        ),
        migrations.AddField(
            model_name='webstore',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.state'),
        ),
    ]
