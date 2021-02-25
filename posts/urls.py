from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<post_id>', views.post_detail, name='post_detail'),
]