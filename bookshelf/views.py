# adoption/views.py
from django.http import HttpResponse
from .models import Book

def index(req):
    return HttpResponse("<h1>Hello! Here are all the books who need adopting!<h1>")

def show(req, id):
    book = Book.objects.get(pk=id)
    return HttpResponse(f'<h3>Book number {id}!</h3><p>{book.name} by {book.author}</p>')