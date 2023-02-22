from django.db import models

# Create your models here.

class Stations(models.Model):
    id_primary = models.CharField(primary_key=True, max_length=50)
    name_station = models.CharField(max_length=55)
    address = models.CharField(max_length=100)
    empty_slot = models.IntegerField()
    altitude = models.IntegerField()
    ebikes = models.IntegerField() 
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment_key = models.BooleanField()
    payment_transitcard = models.BooleanField()
    payment_creditcard = models.BooleanField()
    payment_phone = models.BooleanField()
    #post_code = models.Int(10)
    renting = models.IntegerField()
    returning_val = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=10)
    free_bikes = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    