from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": (
                "w-full px-4 py-2 border border-gray-300 rounded-lg "
                "shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 "
                "focus:border-indigo-500"
            ),
            "placeholder": "Enter username",
        })
    )

    class Meta:
        fields = ['username', 'email', 'password1', 'password2']
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display'
        self.fields['email'].label = "Email Address"
