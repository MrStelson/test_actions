from django.db import models


class City(models.Model):
    name = models.CharField(max_length=128)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
