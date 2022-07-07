from django.shortcuts import render

from .models import Book, CommentOnBook
from .forms import BookModelForm, CommentOnBookForm


def home_view(request, *args, **kwargs):
    book = Book.objects.filter(is_active=True)[0]
    context = {
        "book": book,
    }
    print(book)
    return render(request, "book/index.html", context)


def prev_books_view(request, *args, **kwargs):
    prev_books = Book.objects.filter(is_active=False)
    comments = CommentOnBook.objects.all()
    comment_form = CommentOnBookForm(request.POST or None)
    print("comment_form =", comment_form)
    if request.GET.get("q_book"):
        q_book_title = request.GET.get("q_book").lower()
        prev_books = Book.objects.filter(is_active=False, title__icontains=q_book_title)
    if comment_form.is_valid():
        new_comment = CommentOnBook.objects.create(**comment_form.cleaned_data)
        print("new_comment =", new_comment)
        comment_form = CommentOnBookForm()
    context = {
        "prev_books": prev_books,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "book/prev_books.html", context)


def add_book_view(request, *args, **kwargs):
    form = BookModelForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        print(form.cleaned_data)
        form.save()
        form = BookModelForm()
    context = {"form": form}
    return render(request, "book/add_book.html", context)
