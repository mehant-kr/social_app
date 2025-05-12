# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full border-gray-300 rounded-md shadow-sm p-2 focus:ring-2 focus:ring-indigo-500",
                "rows": 4,
                "placeholder": "What’s on your mind?"
            }
        )
    )

    class Meta:
        model = Post
        fields = ["message", "group"]