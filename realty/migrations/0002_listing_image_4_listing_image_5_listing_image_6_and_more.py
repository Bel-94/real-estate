# Generated by Django 4.0.5 on 2022-06-23 09:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_4',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image_4'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_5',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image_5'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_6',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image_6'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(choices=[('6', '6'), ('5', '5'), ('8', '8'), ('1', '1'), ('10', '10'), ('4', '4'), ('7', '7'), ('9', '9'), ('3', '3'), ('2', '2')]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(choices=[('200000', '$200,000'), ('300000', '$300,000'), ('1000000', '$1M+'), ('900000', '$900,000'), ('400000', '$400,000'), ('600000', '$600,000'), ('800000', '$800,000'), ('500000', '$500,000'), ('100000', '$100,000'), ('700000', '$700,000')]),
        ),
    ]