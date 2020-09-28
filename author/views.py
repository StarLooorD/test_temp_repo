from django.shortcuts import render, redirect
from .models import Author


def author_get_all(request):
    context = {'author_list': Author.objects.all()}
    return render(request, "author/author_form.html", context)


def author_post():
    pass


def author_put():
    pass


def author_delete(request, id):
    author = Author.objects.get(pk=id)
    author.delete()
    return redirect('/author/all/')
