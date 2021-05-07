  # adoption/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookshelf-index'), # route for /adoption/
    path('about/', views.about, name='bookshelf-about'), # route for /adoption/about
    path('books/', views.books, name='bookshelf-books'), # route for /adoption/:id
    path('authors/', views.authors, name='bookshelf-authors'), # route for /adoption/:id
    # path('<id>/', views.show, name='bookshelf-show'), # route for /adoption/:id
    path('books/<int:id>/', views.showbook, name='bookshelf-show'), # to accept only numbers as id param
    path('books/new/', views.create, name='book-create'),
]