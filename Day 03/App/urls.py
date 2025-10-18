from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("authors/<int:author_id>/", views.show_author, name="author-show"),
    path("books/", views.show_books, name="books-show"),
    path("books/<int:book_id>", views.show_book, name="book-show"),
]