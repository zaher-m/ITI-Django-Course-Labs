from django.shortcuts import render

# Create your views here.

def index(request, coursename):
    return render(request, "course/index.html", {"coursename":coursename})