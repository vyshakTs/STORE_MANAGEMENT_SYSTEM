# Generated by Django 3.2 on 2021-05-23 18:38

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('profile_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('dob', models.DateTimeField(verbose_name='Date of birth')),
                ('phone_no', models.IntegerField(verbose_name='Phone number')),
                ('slug', autoslug.fields.AutoSlugField(unique=True)),
                ('current_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.country')),
                ('post_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.postcode')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.state')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
