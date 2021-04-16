from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)

