"""from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=20)
    email = forms.EmailField(max_length=254, help_text='Required Valid address')
    evidence = forms.ImageField()
    gender_choice=[('waman','woman'),('man','man')]
    sex= forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect)
    birth_date = forms.DateTimeField(help_text=' -을 포함하여 년도-월-일로 구분해주세요')
    phone_number = forms.CharField(max_length=11, help_text='전화번호는 - 을 포함하여 형식에 맞게 9-15자리로 써주세요')
    agreement = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')), widget=forms.RadioSelect )
    class Meta:
        model = User
        fields = ('first_name','last_name','username' , 'email', 'evidence', 'sex','birth_date','phone_number','password1','password2','agreement')
    def save(self,commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.sex = self.cleaned_data["sex"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.agreement = self.cleaned_data["agreement"]
        if commit:
            user.save()
        return user

"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Profile2

class SignUpForm2(UserCreationForm):
    test_record = forms.FileField()
    gender_choice=[('woman','woman'),('man','man')]
    sex= forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect())
    birth_date = forms.DateTimeField(help_text='YYYY-MM-DD')
    phone_valid = RegexValidator(regex=r'^\d{3}-\d{3,4}-\d{4}$', message="000-0000-0000")
    phone_number = forms.CharField(validators=[phone_valid],max_length=13)
    agreement1 = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')), widget=forms.RadioSelect )
    agreement2 = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')), widget=forms.RadioSelect )
    """accept_choice=[('yes','yes'),('no','no')]
    agreement1= forms.ChoiceField(choices=accept_choice, widget=forms.RadioSelect)
    agreement2= forms.ChoiceField(choices=accept_choice, widget=forms.RadioSelect)"""
    class Meta:
        model = User 
        fields = ('first_name','last_name','username' , 'email', 'test_record','sex','birth_date','phone_number','password1','password2','agreement1', 'agreement2')
    
    # ohjinjin, 08/03/19 AM 01:52
    # 이 함수 두개는 파라미터 주면서 통일 가능한지 확인해보도록 하겠습니다
    def clean_agreement1(self):
        data = self.cleaned_data.get('agreement1')
        if data == self.fields['agreement1'].choices[0][0]:
            raise forms.ValidationError('agreement1 is required')
        return data
    
    def clean_agreement2(self):
        data = self.cleaned_data.get('agreement2')
        if data == self.fields['agreement2'].choices[0][0]:
            raise forms.ValidationError('agreement2 is required')
        return data
