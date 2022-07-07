from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)
