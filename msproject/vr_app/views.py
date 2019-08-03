from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from .forms import SignUpForm2
from .forms import SignUpForm
from django.contrib import auth
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
##from .models import HelpData
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#from .models import Profile2
import ms_app.models

def index(request): # ohjinjin 함수 추가
    return render(request,'index.html')

def vr_login(request):
    # ohjinjin 함수 전반적으로 수정
    if request.method == "POST":
        username = request.POST['ID']
        password = request.POST['vr_password']
        user = auth.authenticate(request, username = username, password = password1)

        if user is not None:
            auth.login(request,user)
            return render(request, 'index.html', {'ID' : user.username}) # ohjinjin 문장 추가
        else:
            return render(request, 'vr_login.html',{'error' : 'username or password is incorrect.'})
    #return render(request, 'accounts/vr_login.html')
    return render(request, 'vr_login.html') # ohjinjin 문장 추가

"""def vr_signup(request):
    return render(request,'vr_signup.html')"""

    
def logout(request):
    auth.logout(request)
    return redirect('index')

def apply(request): # ohjinjin 함수 추가
    return render(request,'apply.html')

def vr_help(request):
    question = HelpData.objects
    return render(request, 'vr_help.html',{'question':question})

def about(request):
    return render(request, 'about.html')

def vr_index(request):  # 추가 chanho - 19_8_2_13:50
    return render(request, 'vr_index.html')

def qna(request):
    return render(request,'qna.html')

def create(request):
    question = HelpData()
    question.question_title = request.GET['question_title']
    question.question_content = request.GET['question_content']
    question.pub_date =timezone.datetime.now()
    question.save()
    return redirect('vr_help')

class CreateUserView(CreateView):  # 제네릭의 CreateView는 폼하고 연결돼서, 혹은 모델하고 연결돼서 새로운 데이터를 넣을 때 사용.
    template_name = 'vr_signup.html'     # 회원가입 할 때 띄울 폼 템플릿
    form_class = SignUpForm
    success_url = reverse_lazy('vr_index') # 성공하면 어디로 갈지, url name
    # 여기서 reverse가 아닌 reverse_lazy를 사용하는 이유: 제네릭뷰 같은경우 타이밍 문제 때문에 reverse_lazy를 사용해야함

    def form_valid(self,form):
        c = {'form':form,}
        user = form.save(commit=False)  #여기서 default User model과 profile이 엮여서 db에 저장되는듯합니다.
        evidence = form.cleaned_data["evidence"]
        sex = form.cleaned_data["sex"]
        birth_date = form.cleaned_data["birth_date"]
        phone_number = form.cleaned_data["phone_number"]
        agreement = form.cleaned_data["agreement"]
        
        user.save()

        Profile2.objects.create(user=user, phone_number=phone_number, birth_date = birth_date, evidence=evidence,sex=sex,agreement=agreement)

        return super(CreateUserView, self).form_valid(form)

def question_info(request,question_id):
    question = HelpData.objects
    return render(request,'questioin_info',{'question':question})

class RegisteredView(TemplateView): # �쉶�썝媛��엯�씠 �셿猷뚮맂 寃쎌슦
    template_name = 'vr_index.html'



"""class CreateUserView2(CreateView):  # 제네릭의 CreateView는 폼하고 연결돼서, 혹은 모델하고 연결돼서 새로운 데이터를 넣을 때 사용.
    template_name = 'vr_signup.html'     # 회원가입 할 때 띄울 폼 템플릿
    form_class = SignUpForm2
    success_url = reverse_lazy('vr_index') # 성공하면 어디로 갈지, url name
    # 여기서 reverse가 아닌 reverse_lazy를 사용하는 이유: 제네릭뷰 같은경우 타이밍 문제 때문에 reverse_lazy를 사용해야함

    def form_valid(self,form):
        c = {'form':form,}
        user = form.save(commit=False)  #여기서 default User model과 profile이 엮여서 db에 저장되는듯합니다.
        evidence = form.cleaned_data["evidence"]
        sex = form.cleaned_data["sex"]
        birth_date = form.cleaned_data["birth_date"]
        phone_number = form.cleaned_data["phone_number"]
        agreement1 = form.cleaned_data["agreement1"]
        agreement2 = form.cleaned_data["agreement2"]
        
        user.save()

        Profile2.objects.create(user=user, phone_number=phone_number, birth_date = birth_date, evidence=evidence,sex=sex,agreement1=agreement1, agreement2=agreement2)

        return super(CreateUserView2, self).form_valid(form)
"""