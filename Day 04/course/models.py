from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name}"