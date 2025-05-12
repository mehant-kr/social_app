# posts/forms.py
from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": (
                "w-full px-4 py-2 border border-gray-300 rounded-lg "
                "shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 "
                "focus:border-indigo-500"
            ),
            "placeholder": "Enter group name",
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":
                    "w-full px-4 py-2 border border-gray-300 rounded-lg "
                    "shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 "
                    "focus:border-indigo-500"
,
                "rows": 4,
            }
        )
    )


    class Meta:
        model = Group
        fields = ["name", "description"]
