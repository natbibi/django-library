# adoption/views.py
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Book, Author

from .forms import NewBookForm

# change settings DEBUG = False ALLOWED_HOSTS = ['*'] to test
def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')

def index(req):
    return render(req, 'base.html') 

def about(req):
    return render(req, 'about.html') 

def showbook(req, id):
    book = {'book': Book.objects.get(pk=id)}
    return render(req, 'showbook.html', book) 
    # return HttpResponse(f'<h3>Book number {id}!</h3><p>{book.name} by {book.author}</p>')

@login_required
def books(req):
    books = {'books': Book.objects.all()}
    return render(req, 'books.html', books) 

@login_required
def authors(req):
    authors = {'authors': Author.objects.all()}
    return render(req, 'authors.html', authors) 

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            book_id = book.save().id
            return redirect("bookshelf-books")
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'newbook.html', data)