from django.db import models

# Create your models here.


class Style(models.Model):
    style = models.CharField(max_length=100)

    # modify the str representation of Genre object
    def __str__(self):
        return self.style


class Tank(models.Model):
    tank_type = models.CharField(max_length=100)
    barrel_volume = models.IntegerField()
    temp = models.FloatField()
    time_days = models.IntegerField()
    # relation between tables (classes)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    # director = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# class Order(models.Model):
#     client_id = models.IntegerField()
#     total = models. FloatField()

# class Order_Items(models.Model):
#     movie_id: models.IntegerField()
#     quantity: models.IntegerField()
#     order: models.ForeignKey(Order, on_delete=models.CASCADE)

