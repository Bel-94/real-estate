from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
BEDROOMS={

    ('1',('1')),
    ('2',('2')),
    ('3',('3')),
    ('4',('4')),
    ('5',('5')),
    ('6',('6')),
    ('7',('7')),
    ('8',('8')),
    ('9',('9')),
    ('10',('10')),
}

PRICES={
    ('100000',('$100,000')),
    ('200000',('$200,000')),
    ('300000',('$300,000')),
    ('400000',('$400,000')),
    ('500000',('$500,000')),
    ('700000',('$700,000')),
    ('600000',('$600,000')),
    ('800000',('$800,000')),
    ('900000',('$900,000')),
    ('1000000',('$1M+')),

}

COUNTIES = [
    ('', ('Choose')), 
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField('photo', null=True)
    description = models.TextField(max_length=500)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=50)
    hire_date = models.DateTimeField(auto_now_add=True)
    is_mvp = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    county = models.CharField(choices=COUNTIES, max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField(choices=PRICES)
    bedrooms = models.IntegerField(choices=BEDROOMS)
    bathrooms = models.DecimalField(max_digits=10, decimal_places=1)
    sqft = models.IntegerField()
    main_image = CloudinaryField('main_image', null=True)
    image_1 = CloudinaryField('image_1', null=True)
    image_2 = CloudinaryField('image_2', null=True)
    image_3 = CloudinaryField('image_3', null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    


class Contacts(models.Model):
    listing=models.CharField(max_length=200)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(auto_now_add=True, blank=True)
    user_id=models.IntegerField(blank=True)


    def __str__(self):
        return self.name








