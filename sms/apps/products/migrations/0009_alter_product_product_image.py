# Generated by Django 3.2 on 2021-06-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(blank=True, null=True, upload_to='products'),
        ),
    ]
