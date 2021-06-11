from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm
from .models import Book, Author

# Create your views here.

def book_list(request):
    context = {'book_list': Book.objects.all()}
    return render(request, "library_app/book_list.html", {'book_list':Book.objects.all()})

def book_form(request, id = 0):
    print(request.method)
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request, "library_app/book_form.html", {'form':form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/book/list')

def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/book/list')

def author_list(request):
    return render(request, "library_app/author_list.html", {'author_list': Author.objects.all()})

def author_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
        return render(request, "library_app/author_form.html", {'form':form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/author/list')

def author_delete(request, id):
    author = Author.objects.get(pk=id)
    author.delete()
    return redirect('/author/list')
