# Generated by Django 4.0.5 on 2022-06-22 12:09

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='photo')),
                ('description', models.TextField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('hire_date', models.DateTimeField(auto_now_add=True)),
                ('is_mvp', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('county', models.CharField(choices=[('', 'Choose'), ('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma ', 'Bungoma '), ('Busia', 'Busia'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Marsabit', 'Marsabit'), ('Mombasa', 'Mombasa'), ('Muranga', 'Muranga'), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita Taveta', 'Taita Taveta'), ('Tana River', 'Tana River'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField(choices=[('300000', '$300,000'), ('800000', '$800,000'), ('100000', '$100,000'), ('500000', '$500,000'), ('900000', '$900,000'), ('1000000', '$1M+'), ('400000', '$400,000'), ('200000', '$200,000'), ('600000', '$600,000'), ('700000', '$700,000')])),
                ('bedrooms', models.IntegerField(choices=[('3', '3'), ('8', '8'), ('5', '5'), ('6', '6'), ('2', '2'), ('10', '10'), ('1', '1'), ('7', '7'), ('4', '4'), ('9', '9')])),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=10)),
                ('sqft', models.IntegerField()),
                ('main_image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='main_image')),
                ('image_1', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image_1')),
                ('image_2', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image_2')),
                ('image_3', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image_3')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.realtor')),
            ],
        ),
    ]