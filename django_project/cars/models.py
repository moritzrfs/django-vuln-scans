from django.db import models

# Create your models here.
class Car(models.Model):
    creator = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    seats = models.IntegerField()
    doors = models.IntegerField()
    engine = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EvCar(Car):
    class Meta:
        proxy = True
    
    # only ev vehicles return
    def get_queryset(self):
        return super().get_queryset().filter(engine='electric')
    
    def __str__(self):
        return self.name
