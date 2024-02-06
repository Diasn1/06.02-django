from django.contrib import admin
from .models import Animal, Enclosure
# Register your models here.

admin.site.register([
    Animal,
    Enclosure,
])