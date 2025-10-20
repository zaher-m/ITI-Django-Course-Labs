from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import Student
from .forms import StudentForm


def student_list(request):
    try:
        students = Student.get_students()
    except Http404:
        students = [] 
    return render(request, 'student/list.html', {'students': students})

# Create Student (manual form)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = Student.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                image=form.cleaned_data['image'],
                dob=form.cleaned_data['dob']
            )
            course_ids = form.cleaned_data.get('courses', [])
            for course_id in course_ids:
                student.courses.add(course_id)
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/create.html', {'form': form})

# Update Student (manual form)
def student_update(request, pk):
    student = Student.get_student(pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.age = form.cleaned_data['age']
            if form.cleaned_data.get('image'):
                student.image = form.cleaned_data['image']
            student.dob = form.cleaned_data['dob']
            student.save()

            student.courses.clear()
            for course_id in form.cleaned_data.get('courses', []):
                student.courses.add(course_id)
            return redirect('student_list')
    else:
        initial_data = {
            'name': student.name,
            'age': student.age,
            'dob': student.dob,
            'courses': [c.code for c in student.courses.all()],
        }
        form = StudentForm(initial=initial_data)
    return render(request, 'student/update.html', {'form': form, 'student': student})

# Delete
def student_delete(request, pk):
    student = Student.get_student(pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student/delete.html', {'student': student})
