from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#from .forms import SignUpForm  ohjinjin 앱 새로 생성하면서 당장은 필요없어져서 주석처리합니다
# Create your views here.

def index(request): # ohjinjin 함수 추가
    return render(request,'index.html')

def vr_login(request):
    # ohjinjin 함수 전반적으로 수정
    if request.method == "POST":
        username = request.POST['ID']
        password = request.POST['vr_password']
        user = auth.authenticate(request, username = ID, password = vr_password)

        if user is not None:
            auth.login(request,user)
            return render(request, 'index.html', {'ID' : user.email}) # ohjinjin 문장 추가
        else:
            return render(request, 'vr_login.html',{'error' : 'username or password is incorrect.'})
    #return render(request, 'accounts/vr_login.html')
    return render(request, 'vr_login.html') # ohjinjin 문장 추가

def vr_signup(request):
    return render(request,'vr_signup.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')

def apply(request): # ohjinjin 함수 추가
    return render(request,'apply.html')

def vr_help(request):
    return render(request, 'vr_help.html')