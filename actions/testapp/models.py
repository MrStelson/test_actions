"""This module for init db models"""
from django.db import models


class City(models.Model):
    """Model city"""
    name = models.CharField(max_length=128)
    objects = models.Manager()


class User(models.Model):
    """Model user"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    objects = models.Manager()
