from django.shortcuts import render, redirect, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

def course_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Course.objects.create(name=name.strip())
            return redirect('course_list')
        else:
            error = "Course name cannot be empty!!"
            return render(request, 'course/create.html', {'error': error})
    
    return render(request, 'course/create.html')

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    print(course)
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        if name:
            course.name = name.strip()
            course.save()
            return redirect('course_list')
        else:
            error = "Course name cannot be empty!!!"
            return render(request, 'course/update.html', {'error': error, 'course': course})
    
    return render(request, 'course/update.html', {'course': course})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course/delete.html', {'course': course})
