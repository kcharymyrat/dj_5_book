from dataclasses import fields
from django import forms

from .models import Book, CommentOnBook


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "slug", "author", "content")
        widgets = {
            "comment": forms.Textarea(attrs={"placeholder": "Insert the comment"})
        }

    def clean_author(self):
        data = self.cleaned_data.get("author")
        if len(data) < 4:
            raise forms.ValidationError(
                "Author name is too short, must be at least 2 chars"
            )
        return data


class CommentOnBookForm(forms.Form):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"placeholder": "Insert your comments here"}),
    )

    def clean_comment(self):
        data = self.cleaned_data.get("comment")
        if len(data) < 2:
            raise forms.ValidationError(
                "Your comment should be at least 2 charactes long!"
            )
        return data
