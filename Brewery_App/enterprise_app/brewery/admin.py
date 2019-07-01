from django.contrib import admin
from .models import Genre, Movie


class StyleAdmin(admin.ModelAdmin):
    list_display = ('style', ' barrel_volume')  # tuple


class TankAdmin(admin.ModelAdmin):
 
    list_display = ('tank_type', 'barrel_volume', 'temp', 'time_days')  # props on the list table


    # Register your models here.
admin.site.register(Style, StyleAdmin)
admin.site.register(Tank, TankAdmin)
