from django.shortcuts import render,redirect
from .models import *
from ..users.models import *
from django.contrib import messages
def index(request):
    context={
        'reviews':Review.objects.all().values(),
        'books':Book.objects.all().values(),
        'currentuser':User.objects.all().values().get(email=request.session['email'])
    }
    return render(request, 'books/index.html', context)