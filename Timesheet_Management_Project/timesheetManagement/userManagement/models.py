from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    email=models.CharField(max_length=25)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname

