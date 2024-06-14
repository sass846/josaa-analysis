from django.db import models

# Create your models here.

class josaa(models.Model):
    institute = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    quota = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    opening_rank = models.IntegerField()
    closing_rank = models.IntegerField()
    preparatory = models.BooleanField()