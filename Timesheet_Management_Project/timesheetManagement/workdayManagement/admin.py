from django.contrib import admin

# Register your models here.
from workdayManagement.models import Workday,Location

admin.site.register(Workday)
admin.site.register(Location)
