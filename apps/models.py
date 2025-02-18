from django.db import models
from django.db.models import Model, TextChoices, CharField, ImageField, TextField, DateField, PositiveIntegerField, \
    DecimalField, ForeignKey, CASCADE, EmailField, DateTimeField


class City(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='cities/')
    description = TextField()
    date = DateField(auto_now=True)
    duration = PositiveIntegerField(default=1)
    price = DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class Attraction(Model):
    city = ForeignKey(City, CASCADE, related_name='attractions')
    name = CharField(max_length=255)
    image = ImageField('attractions/')
    description = TextField()

    def __str__(self):
        return self.name

class About(Model):
    image1 = ImageField(upload_to='abouts/')
    image_interior = ImageField(upload_to='abouts/')
    description = TextField()
    description_interior = TextField()

    def __str__(self):
        return self.description

class ContactInfo(Model):
    address = CharField(max_length=255)
    phone1 = CharField(max_length=20)
    phone2 = CharField(max_length=20)
    email = EmailField()

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = CharField(max_length=255)
    phone = CharField(max_length=20)
    message = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transport(Model):
    name = CharField(max_length=255)
    image_exterior = ImageField(upload_to='transports/')
    image_interior = ImageField(upload_to='transports/')
    description_exterior = TextField()
    description_interior = TextField()

    def __str__(self):
        return self.name


class CityImage(models.Model):
    city = models.ForeignKey(City, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return f"{self.city.name}"

