from django.urls import path
from . import views

urlpatterns = [
    # path("student/", views.show_student, name="std-show")
    path("home/", views.index, name="home"),
    path("student/delete/<int:std_id>/", views.delete_student, name="std-delete"),
    path("student/<int:std_id>/", views.show_student, name="std-show"),
    path("student/deleted/", views.show_deleted_students, name="deleted"),
]