from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book

# Create your views here.
def viewBooks(request):
    if 'userid' in request.session:
        print(f'user accessing books app')
        context = {
            'user': User.objects.get(id = request.session['userid']),
            'all_books': Book.objects.all()
        }
    else:
        return redirect(f'/')
    return render(request, "fav_books_app/fav_books.html", context)

def addBook(request):
    if request.method == "POST":
        if 'userid' in request.session:
            print(request.POST)
        new_book = Book.objects.create(title=request.POST["new_book"], 
        desc=request.POST["new_description"], 
        uploaded_by=User.objects.get(id=request.session['userid']))
        user = User.objects.get(id = request.session['userid'])
        new_book.users_who_like.add(user)
    return redirect(f'/books')

def addFavorite(request):
    if request.method == "POST":
        if 'userid' in request.session:
            print(request.POST)
            new_fav = Book.objects.get(id=request.POST['book_id'])
            print(new_fav.title)
            user = User.objects.get(id = request.session['userid'])
            new_fav.users_who_like.add(user)
    return redirect(f'/books')

def delFavorite(request):
    if request.method == "POST":
        if 'userid' in request.session:
            print(request.POST)
            old_fav = Book.objects.get(id=request.POST['book_id'])
            print(old_fav.title)
            user = User.objects.get(id = request.session['userid'])
            old_fav.users_who_like.remove(user)
    return redirect(request.META.get('HTTP_REFERER'))

def bookInfo(request, bookID):
    print(f'book info method')
    if 'userid' in request.session:
        context = {
            'user': User.objects.get(id = request.session['userid']),
            'book_info': Book.objects.get(id=bookID),
            'users_who_like': Book.objects.get(id=bookID).users_who_like.all()
        }
    return render(request, "fav_books_app/book_info.html", context)
