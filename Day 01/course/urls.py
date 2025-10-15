from django.urls import path
from . import views

urlpatterns = [
    path("<str:coursename>/", views.index, name="index")
]