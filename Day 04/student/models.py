from django.db import models
from django.shortcuts import get_object_or_404, get_list_or_404
from course.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='student/')
    dob = models.DateField()
    courses = models.ManyToManyField(Course, related_name='students')
    
    @classmethod
    def get_student(cls , id ):
        return get_object_or_404(cls , pk = id)

    @classmethod
    def get_students(cls):
        return get_list_or_404(cls)
    
    def __str__(self):
        return self.name

