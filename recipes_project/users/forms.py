from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=70)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username', 'password1', 'password2')
