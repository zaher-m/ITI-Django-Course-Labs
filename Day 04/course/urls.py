from django.urls import path
from . import views 


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('<str:pk>/update/', views.course_update, name='course_update'),
    path('<str:pk>/delete/', views.course_delete, name='course_delete'),
]