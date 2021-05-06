# adoption/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.name}'