from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=20)
    email = forms.EmailField(max_length=254, help_text='Required Valid address')
    evidence  = forms.FileField(required=False)
    gender_choice=[('woman','woman'),('man','man')]
    sex= forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect)
    birth_date = forms.DateTimeField(help_text=' - 로 년도/월/일을 구분해주세요')
    phone_number = forms.CharField(max_length=11, help_text=' 숫자만 입력해주세요')
    agreement_choice =[('yes','yes'),('no','no')]
    agreement = forms.ChoiceField(choices=agreement_choice, widget=forms.RadioSelect)
    class Meta:
        model = User
        fields = ('name','username' , 'email', 'evidence','sex','birth_date','phone_number','password1','password2','agreement')
    def save(self,commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.evidence = self.cleaned_data["evidence"]
        user.sex = self.cleaned_data["sex"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.agreement = self.cleaned_data["agreement"]
        if commit:
            user.save()
        return user