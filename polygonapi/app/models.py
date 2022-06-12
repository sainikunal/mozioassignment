from django.db import models

# Create your models here.

LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('HIN', 'Hindi'),
]

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('INR', 'Indian Rupee'),
]


class Provider(models.Model):
    """
    This class defines the property and attributes of each provider
    name -> name of the provider (CharField)
    email -> email of the provider (EmailField)
    phonenumber -> phone number of provider (Integer Field)
    language -> language options to choose from LANGUAGE_CHOICES (CharField)
    currency -> currency options to choose from CURRENCY_CHOICES (CharField)
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    """
    This class defines the property and attributes of a polygon
    It has the following fields:
    provider -> Reference to Provider (ForeignKey)
    price -> Price for each polygon (DecimalField)
    geojson -> Dimensions of each polygon (TextField)
    """
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='poly')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    geojson = models.TextField()

    def __str__(self):
        return self.name
