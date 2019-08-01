from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignUpForm
# Create your views here.

def index(request): # ohjinjin 함수 추가
    return render(request,'index.html')

def ms_signup(request):
    if request.method == 'POST':
        if request.POST['ms_password1'] == request.POST['ms_password2']:
            ms_user = User.objects.create_user(request.POST['ms_username'],email=request.POST['ms_email'],password=request.POST['ms_password1'])
            auth.login(request, ms_user)
            return redirect('index.html') # ms 페이지 이동
    #return render(request, 'accounts/ms_signup.html')
    return render(request, 'ms_signup.html',{'error':'회원가입 실패'})    # ohjinjin 문장 수정

def vr_login(request):
    # ohjinjin 함수 전반적으로 수정
    if request.method == "POST":
        username = request.POST['vr_email']
        password = request.POST['vr_password']
        user = auth.authenticate(request, username = email, password = password)

        if user is not None:
            auth.login(request,user)
            return render(request, 'index.html', {'username' : user.email}) # ohjinjin 문장 추가
        else:
            return render(request, 'vr_login.html',{'error' : 'username or password is incorrect.'})
    #return render(request, 'accounts/vr_login.html')
    return render(request, 'vr_login.html') # ohjinjin 문장 추가

def ms_signup(request):
    #return render(request, 'accounts/vr_signup.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.file = self.cleaned_data.get('file')
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'ms_signup.html',{'form':form})    # ohjinjin 문장 추가

def vr_signup(request):
    return render(request,'vr_signup.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')