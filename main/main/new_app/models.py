from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    HEALTH_STATUS_CHOICES = [
        ('healthy', 'Здоровый'),
        ('sick', 'Больной'),
        ('unchecked', 'Не обследованный'),
    ]
    health_status = models.CharField(max_length=20, choices=HEALTH_STATUS_CHOICES)

    def __str__(self):
        return self.name

class Enclosure(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        return self.name