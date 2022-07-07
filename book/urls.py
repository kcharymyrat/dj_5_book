from django.urls import path

from .views import (
    home_view,
    prev_books_view,
    add_book_view,
)

app_name = "book"
urlpatterns = [
    path("", home_view, name="home"),
    path("prev_books", prev_books_view, name="prev_books"),
    path("add_book", add_book_view, name="add_book"),
]
