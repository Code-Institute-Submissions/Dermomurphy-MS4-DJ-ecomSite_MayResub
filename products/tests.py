from django.test import TestCase
from products.models import Product, Brewery

# Create your tests here.

class ProductTestCase(TestCase):
    def setUp(self):
        Products.objects.create(brewery='Brewery1', sku='pp999999',name='Test Name',style='Lager', description='Text Description', abv=3.0,ibu=29, price=3.99,rating=3.45,image_url='https://image.com', image='noimage.png')

   