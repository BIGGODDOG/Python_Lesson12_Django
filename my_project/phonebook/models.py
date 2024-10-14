from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_phone = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Contact: {self.name} ({self.contact_phone})"