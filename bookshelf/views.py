# adoption/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Book

def index(req):
    return render(req, 'base.html') 

def about(req):
    return render(req, 'about.html') 

def show(req, id):
    book = Book.objects.get(pk=id)
    return HttpResponse(f'<h3>Book number {id}!</h3><p>{book.name} by {book.author}</p>')

@login_required
def books(req):
    books = {'books': Book.objects.all()}
    return render(req, 'show.html', books) 