from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
#from .models import Profile
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm # 장고의 기본적인 회원가입 폼. id, password만 확인한다는 한계점.
from django.urls import reverse_lazy
from django.contrib import auth
from .models import Profile

# Create your views here.
"""def ms_signup(request):
    if request.method == 'POST':
        if request.POST['ms_password1'] == request.POST['ms_password2']:
            ms_user = User.objects.create_user(request.POST['ms_username'],email=request.POST['ms_email'],password=request.POST['ms_password1'])
            auth.login(request, ms_user)
            return redirect('index.html') # ms 페이지 이동
    #return render(request, 'accounts/ms_signup.html')
    return render(request, 'ms_signup.html',{'error':'회원가입 실패'})    # ohjinjin 문장 수정"""

class CreateUserView(CreateView):  # 제네릭의 CreateView는 폼하고 연결돼서, 혹은 모델하고 연결돼서 새로운 데이터를 넣을 때 사용.
    template_name = 'ms_signup.html'     # 회원가입 할 때 띄울 폼 템플릿
    form_class = SignUpForm
    success_url = reverse_lazy('ms_index') # 성공하면 어디로 갈지, url name
    # 여기서 reverse가 아닌 reverse_lazy를 사용하는 이유: 제네릭뷰 같은경우 타이밍 문제 때문에 reverse_lazy를 사용해야함

    def form_valid(self,form):
        c = {'form':form,}
        user = form.save(commit=False)  #여기서 default User model과 profile이 엮여서 db에 저장되는듯합니다.
        #email = form.cleaned_data["email"]
        #password1 = form.cleaned_data['password1']
        #password2 = form.cleaned_data['password2']
        evidence = form.cleaned_data["evidence"]
        sex = form.cleaned_data["sex"]
        birth_date = form.cleaned_data["birth_date"]
        phone_number = form.cleaned_data["phone_number"]
        agreement = form.cleaned_data["agreement"]
        
        """if password1 != password2:
            messages.error(self.request, "Passwords do not Match", extra_tags = 'alert alert-danger')
            return render(self.request, self.template_name, c)"""
        #user.set_password(password1)
        user.save()

        Profile.objects.create(user=user, phone_number=phone_number, birth_date = birth_date, evidence=evidence,sex=sex,agreement=agreement)

        return super(CreateUserView, self).form_valid(form)


class RegisteredView(TemplateView): # 회원가입이 완료된 경우
    template_name = 'ms_index.html'

def lists(request): # ohjinjin 08/02/19 AM 10:22 일부러 list말고 lists로 둔겁니당~
    return render(request,'list.html')

def ms_login(request):
    # ohjinjin �븿�닔 �쟾諛섏쟻�쑝濡� �닔�젙
    if request.method == "POST":
        username = request.POST['ID']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        
        if user is not None:
            auth.login(request,user)
            return render(request, 'ms_index.html', {'username' : user.username}) # ohjinjin 臾몄옣 異붽��
        else:
            return render(request, 'ms_login.html',{'error' : 'username or password is incorrect.'})
    #return render(request, 'accounts/vr_login.html')
    return render(request, 'ms_login.html') # ohjinjin 臾몄옣 異붽��

def ms_index(request):
    return render(request, 'ms_index.html')

def ms_library(request):
    return render(request, 'ms_library.html')

"""ohjinjin 여기 왜 이친구가 있는지 모르겠어서 주석처리해놓겠습니다!08/02/19 AM10:05
def vr_index(request):
    return render(request, 'vr_index.html')"""
    
def about(request):
    return render(request, 'about.html')

def wish_books(request):
    return render(request, 'wish_books.html')



