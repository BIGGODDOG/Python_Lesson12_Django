from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Category: {self.name}"
    
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room: {self.name}"
    
class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.room_id} for user {self.user_id.username}"
    
class Amenity(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Room, related_name="amenities")

    def __str__(self) -> str:
        return f"Amenity: {self.name}"