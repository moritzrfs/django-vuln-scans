from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    seats = models.IntegerField()
    doors = models.IntegerField()
    engine = models.CharField(max_length=100)

    def __str__(self):
        return self.name
