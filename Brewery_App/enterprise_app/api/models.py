from django.db import models
from tastypie.resources import ModelResource, ALL
from movies.models import Movie, Genre
from tastypie.authorization import Authorization

# Create your models here.

class GenreResource(ModelResource):
    class Meta:
        resource_name = 'genres'
        queryset = Genre.objects.all()

class MovieResource(ModelResource):
    class Meta:
        resource_name = 'movies'
        queryset = Movie.objects.all()
        filtering = {'price': ALL, 'stock': ALL}

class Order_ItemsResource(ModelResource):
    class Meta:
        resource_name = 'orderitems'
        queryset = Order_Items.objects.all()

class OrderResource(ModelResource):
    class Meta:
        resource_name = 'orders'
        queryset = Order.objects.all()
        allowed_method = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()
