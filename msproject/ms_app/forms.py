from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Profile
class SignUpForm(UserCreationForm):
    #password1 = forms.CharField(widget=forms.PasswordInput)  # test ...ing
    #password2 = forms.CharField(widget = forms.PasswordInput) # test ...ing
    #email = forms.EmailField(widget=forms.EmailInput, help_text='Required Valid address')
    #evidence  = forms.FileField(required=False)  # 수정 chanho - 19_8_2_11:43
    evidence = forms.ImageField() # 추가 chanho - 19_8_2_11:43
    gender_choice=[('woman','woman'),('man','man')]
    sex= forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect)
    birth_date = forms.DateTimeField(help_text='-을 포함하여 년도-월-일로 구분해주세요')
    phone_valid = RegexValidator(regex=r'^\d{3}-\d{3,4}-\d{4}$', message="전화번호는 - 을 포함하여 형식에 맞게 9-15자리로 써주세요")
    phone_number = forms.CharField(validators=[phone_valid],max_length=13)
    agreement = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')), widget=forms.RadioSelect )
    class Meta:
        model = User 
        fields = ('first_name','last_name','username' , 'email', 'evidence','sex','birth_date','phone_number','password1','password2','agreement') #evidence 제외 # 추가 chanho - 19_8_2_11:43
    """def save(self,commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        #user.evidence = self.cleaned_data["evidence"]
        user.evidence = self.cleaned_data["evidence"] # 추가 chanho - 19_8_2_11:43
        user.sex = self.cleaned_data["sex"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.agreement = self.cleaned_data["agreement"]
        if commit:
            user.save()
        return user"""
    def clean_agreement(self):
        data = self.cleaned_data.get('agreement')
        if data == self.fields['agreement'].choices[0][0]:
            raise forms.ValidationError('agreement is required')
        return data