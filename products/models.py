from django.db import models


# Create your models here.
class Brewery (models.Model):

    COUNTRIES = [
        ('UK', 'United Kingdom'),
        ('IRL', 'Ireland'),
        ('USA', 'United States'),
        ('GER', 'Germany'),
    ]

    class Meta:
        verbose_name_plural = 'Breweries'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True, choices=COUNTRIES)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
    def get_brewery_country(self):
        return self.country



class Product(models.Model):
    BEER_STYLES = [
        ('IPA', 'India Pale Ale'),
        ('LAGER', 'Lager'),
        ('STOUT', 'Stout'),
        ('ALE', 'Ale'),
        ('PORTER', 'Porter'),
        ('WHEAT', 'Wheat Beer')
    ]

    brewery = models.ForeignKey('Brewery', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    style = models.CharField(max_length=254, choices=BEER_STYLES)
    description = models.TextField()
    abv = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ibu = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name