from django.contrib import admin
from .models import Book, CommentOnBook

admin.site.register(Book)
admin.site.register(CommentOnBook)
