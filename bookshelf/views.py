# adoption/views.py
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Book

def index(req):
    return render(req, 'base.html') 

def show(req, id):
    book = Book.objects.get(pk=id)
    return HttpResponse(f'<h3>Book number {id}!</h3><p>{book.name} by {book.author}</p>')