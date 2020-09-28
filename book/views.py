from django.shortcuts import render, redirect
from .models import Book


def book_list(request):
    book1 = Book(id=101, name="book1", description="description1", count=1)
    book1.save()
    book2 = Book(id=102, name="book2", description="description2")
    book2.save()
    book3 = Book(id=103, name="book3", description="description3")
    book3.save()
    context = {'book_list': Book.objects.all()}
    return render(request, "book/book_form.html", context)


def book_add(request):
    pass


def book_update(request, id=0):
    pass


def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/book/all/')
