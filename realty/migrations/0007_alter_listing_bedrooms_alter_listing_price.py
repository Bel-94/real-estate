# Generated by Django 4.0.5 on 2022-06-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0006_alter_listing_bedrooms_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(choices=[('2', '2'), ('5', '5'), ('8', '8'), ('10', '10'), ('3', '3'), ('9', '9'), ('7', '7'), ('6', '6'), ('1', '1'), ('4', '4')]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(choices=[('$100,000', '100,000'), ('$200,000', '200,000')]),
        ),
    ]