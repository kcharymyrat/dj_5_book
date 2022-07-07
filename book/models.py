from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, id#{self.id}"


class CommentOnBook(models.Model):
    comment = models.TextField()

    def __str__(self) -> str:
        return f"{self.comment}"
