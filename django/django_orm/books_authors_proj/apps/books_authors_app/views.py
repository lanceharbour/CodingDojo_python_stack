from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    books = {
        "book_list": Book.objects.all()
    }
    return render(request, "books_authors_app/index.html", books)

def authors(request):
    authors = {
        "author_list": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", authors)

def displayBookInfo(request, number):
    book_data = {
        "book_info": Book.objects.get(id=number),
        "book_authors": Book.objects.get(id=number).authors.all(),
        "author_list": Author.objects.all()
    }
    return render(request, "books_authors_app/book_info.html", book_data)

def displayAuthorInfo(request, number):
    author_data = {
        "author_info": Author.objects.get(id=number),
        "author_books": Author.objects.get(id=number).books.all(),
        "book_list": Book.objects.all()
    }
    return render(request, "books_authors_app/author_info.html", author_data)

def addBook(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST["new_book"], desc=request.POST["new_description"])
    return redirect("/")

def addAuthor(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["new_note"])
    return redirect("/authors")

def addAuthorToBook(request):
    if request.method == "POST":
        print(request.POST)
        (Book.objects.get(id=request.POST['book_id'])).authors.add(Author.objects.get(id=request.POST['author_id']))
    return redirect(request.META.get('HTTP_REFERER'))

def addBookToAuthor(request):
    if request.method == "POST":
        (Author.objects.get(id=request.POST['author_id'])).books.add(Book.objects.get(id=request.POST['book_id']))
    return redirect(request.META.get('HTTP_REFERER'))
