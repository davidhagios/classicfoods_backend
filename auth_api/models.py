from django.db import models
from django.contrib.auth.models import User


# Task Model
class menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    desc = models.TextField(max_length=10000)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title