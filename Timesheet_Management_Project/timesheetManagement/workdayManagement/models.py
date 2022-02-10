from django.db import models
from datetime import date

# Create your models here.

from userManagement.models import User


class Location(models.Model):
    location=models.CharField(max_length=50)
    sector=models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Workday(models.Model):
    work_date=models.DateField(default=date.today)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time_in=models.TimeField()
    time_out=models.TimeField()
    hours_code=models.CharField(max_length=5)









