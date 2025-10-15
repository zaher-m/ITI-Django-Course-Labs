from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


STUDENTS = [
    {
        "name": "Zaher",
        "age":25,
        "id":11,
        "img": "avatar.png"
    },
    
    {
        "name": "Ahmed",
        "age":25,
        "id":12,
        "img": "ah-avatar.png"
    },
    {
        "name": "ALi",
        "age":25,
        "id":13,
        "img": "al-avatar.png"
    },
    # {
    #     "name": "adad",
    #     "id":14,
    #     "age":25,
    #     "img": "al-avatar.png"
    # },

]

REMOVED_STUDENTS = []

def index(request):
    # return HttpResponse("HELLO")
    return render(request, "App/home.html", context={"students":STUDENTS})

def show_student(request, std_id):
    student = next((s for s in STUDENTS if s["id"] == std_id), None)
    return render(request, "App/student.html", {"student": student})
    # return render(request, "App/student.html", {"std_id":std_id, "students":students})

def delete_student(request, std_id):
    student = next((s for s in STUDENTS if s["id"] == std_id), None)
    if student: 
        REMOVED_STUDENTS.append(student)
        STUDENTS.remove(student)

    print(STUDENTS)
    return render(request, "App/home.html", {"students":STUDENTS})  

def show_deleted_students(request):
    return render(request, "App/deleted.html", context={"students":REMOVED_STUDENTS})