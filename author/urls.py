from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.author_get_all, name='author_all'),  # shows the list of all books
    path('add/', views.author_post, name='author_add'),  # creates book
    path('update/<int:id>', views.author_put, name='author_update'),  # updates the book
    path('delete/<int:id>', views.author_delete, name='author_delete'),  # deletes the book
]