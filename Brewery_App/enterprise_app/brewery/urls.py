from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('configuration', views.index, name="configuration"),
    path('detail/<:tank_type>', views.detail, name="detail"),

    path('genres', views.genres, name="genres"),

    # path('test', views.test, name="test"),
    # path('contact', views.contact, name="contat"),
    # path('contactme', views.contact, name="contactme"),
    # path('history', views.history, name="history"),
    # path('order', views.order, name="order")
]
