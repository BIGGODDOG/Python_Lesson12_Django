from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model  = models.CharField(max_length=100)
    year = models.IntegerField()
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(blank=True, null=True)
    # image = models.ImageField(upload_to="room_images/", blank=True, null=True)

    def __str__(self):
        return f"Car: {self.make}, {self.model} ({self.year}): {self.price}"
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    purchased_cars = models.ManyToManyField(Car, related_name="cars")

    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name} ({self.email})"