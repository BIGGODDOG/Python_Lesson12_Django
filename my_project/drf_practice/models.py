from django.contrib.auth.models import User
from django.db import models

class User(models.Model):  # Расширяем базовую модель пользователя
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_id.username

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title