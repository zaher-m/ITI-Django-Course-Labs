

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request, name):
    return render(request, "student/index.html", {"name":name})
    return HttpResponse("Hello, world from student's view.")