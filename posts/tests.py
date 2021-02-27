from django.test import TestCase
from posts.models import Posts
from datetime import datetime
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        Posts.objects.create(title='Test1', body='TEst text',created_on=datetime.now)
