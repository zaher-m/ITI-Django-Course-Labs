from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from App.models import Book, Author


def home(request):
    return render(request, "App/home.html")

def show_books(request):
    objects = Book.objects.all() 
    context = {"objects": objects}
    return render(request, "App/books.html", context)

def show_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "App/book.html", context={"book":book})
def show_author(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
        author_books = Book.objects.filter(auther=author)
        return render(request, "App/author.html", context={"author":author, "author_books":author_books})
    except:
        return render(request, "App/notfound.html")
