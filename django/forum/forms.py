from django import forms
from .models import Board, Post, Thread


class NewBoardForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Give a short description"}
        ),
        max_length=30,
        help_text="The max length of the text is 30.",
    )

    class Meta:
        model = Board
        fields = ["title", "description"]



class NewThreadForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 5, "placeholder": "What is on your mind?"}
        ),
        max_length=255,
        help_text="The max length of the text is 255.",
    )

    class Meta:
        model = Thread
        fields = ["title", "message"]


class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 5, "placeholder": "What is on your mind?"}
        ),
        max_length=4000,
        help_text="The max length of the text is 4000.",
    )

    class Meta:
        model = Post
        fields = ["message"]

