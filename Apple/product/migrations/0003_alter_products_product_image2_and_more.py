# Generated by Django 4.2.3 on 2023-07-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_products_varient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_image2'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to='product_image3'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image4',
            field=models.ImageField(blank=True, null=True, upload_to='product_image4'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image5',
            field=models.ImageField(blank=True, null=True, upload_to='product_image5'),
        ),
    ]