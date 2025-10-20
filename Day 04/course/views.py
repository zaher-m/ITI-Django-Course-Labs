from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

# List Courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            Course.objects.create(
                code=form.cleaned_data['code'],
                name=form.cleaned_data['name']
            )
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/create.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course.code = form.cleaned_data['code']
            course.name = form.cleaned_data['name']
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm(initial={
            'code': course.code,
            'name': course.name
        })
    return render(request, 'course/update.html', {'form': form, 'course': course})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course/delete.html', {'course': course})
