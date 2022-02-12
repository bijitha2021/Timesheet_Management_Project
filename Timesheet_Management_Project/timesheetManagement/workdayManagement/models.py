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

    def clean(self, *args, **kwargs):
        from django.core.exceptions import ValidationError
        if self.time_out < self.time_in:
            raise ValidationError("Time_out cannot be less than Time_in")
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)









