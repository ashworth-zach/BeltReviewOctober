from django.shortcuts import render,redirect
from .models import *
from ..users.models import *
from django.contrib import messages
def index(request):
    if 'email' not in request.session:
        return redirect('/')
    context={
        'reviews':Review.objects.all(),
        'books':Book.objects.all().values(),
        'currentuser':User.objects.all().values().get(email=request.session['email'])
    }
    return render(request, 'books/index.html', context)
def addbook(request):
    if 'email' not in request.session:
        return redirect('/')
    context={
        'user':User.objects.get(email=request.session['email'])
    }
    return render(request, 'books/newbook.html')
def newbook(request):
    if 'email' not in request.session:
        return redirect('/')
    flag=False
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Book.objects.basic_validator(request.POST)
    errors1 = Review.objects.basic_validator(request.POST)
    # check if the errors object has anything in it
    
    if len(errors):
        flag=True
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
    if len(errors1):
        flag=True
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors1.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
    if flag:
        return redirect('/books/add')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        this_user=User.objects.get(email=request.session['email'])
        this_book=Book.objects.create()
        this_book.title=request.POST['title']
        this_book.author=request.POST['author']
        this_book.desc=request.POST['desc']
        this_book.save()
        review=Review.objects.create(user=this_user,book=this_book,rating=request.POST['rating'],content=request.POST['content'])

        messages.success(request, "Book successfully posted")
        # redirect to a success route
        return redirect('/books')
def show(request, bookid):
    context={
        'book':Book.objects.get(id=bookid),
        'reviews':Review.objects.filter(book=bookid)
    }
    return render(request, 'books/show.html', context)
def addreview(request):
    errors = Review.objects.basic_validator(request.POST)
    bookid=request.POST['bookid']
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/books/'+str(bookid))
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        this_user=User.objects.get(email=request.session['email'])
        this_book=Book.objects.get(id=bookid)
        review=Review.objects.create(user=this_user,book=this_book,rating=request.POST['rating'],content=request.POST['content'])

        messages.success(request, "review successfully posted")
        return redirect('/books/'+str(bookid))