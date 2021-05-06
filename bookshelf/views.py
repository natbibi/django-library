# adoption/views.py
from django.http import HttpResponse

def index(req):
    return HttpResponse("<h1>Hello! Here are all the books who need adopting!<h1>")

def show(req, id):
    return HttpResponse(f'<h3>Book number {id}!</h3>')