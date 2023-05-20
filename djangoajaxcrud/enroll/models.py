from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    passowrd = models.CharField(max_length=100)
