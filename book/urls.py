from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.book_list, name='book_all'),  # shows the list of all books
    path('add/', views.book_add, name='book_add'),  # creates book
    path('update/<int:id>', views.book_update, name='book_update'),  # updates the book
    path('delete/<int:id>', views.book_delete, name='book_delete'),  # deletes the book
]
