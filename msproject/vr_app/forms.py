from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required Valid address')
    file  = forms.FileField()
    userid = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','userid' , 'email', 'file','password1','password2')