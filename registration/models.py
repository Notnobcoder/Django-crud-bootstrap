from django.db import models

# Create your models here.
class Registraion_model(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.CharField(max_length=10)