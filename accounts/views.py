from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import forms

def logout_view(request):
    logout(request)
    return redirect('thanks')

class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login') # when someone has successfull signup,
                                        # i will reverse back to 'login' page
    template_name = 'accounts/signup.html'