from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    def __str__(self):
        return self.name


