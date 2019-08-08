from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm2
#from .forms import SignUpForm
from django.contrib import auth
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import HelpData
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile2
import ms_app.models
from django.core.paginator import Paginator
# from django.contrib import messages
# from .models import Comment

def index(request): # ohjinjin 함수 추가
    return render(request,'index.html')

def vr_login(request):
    # 해당 쿠키에 값이 없을 경우 None을 return 한다.
    if request.COOKIES.get('inputid') is not None:
        username = request.COOKIES.get('inputid')
        password = request.COOKIES.get('inputpassword')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("vr_index")  
        else:
            return render(request, "vr_login.html")
    elif request.method == "POST":
        username = request.POST["inputid"]
        password = request.POST["inputpassword"]
        # 해당 user가 있으면 username, 없으면 None
        user = auth.authenticate(request, username=username, password=password)
        obj = None
        # msg = ""
        for eachProf in Profile2.objects.all():
            if eachProf.user.username == username:
                obj = eachProf
                break
        if user is not None and obj is not None :
            auth.login(request, user)
            if request.POST.get("keep_login") == "TRUE":
                response = render(request, 'vr_index.html')
                response.set_cookie('inputid',username)
                response.set_cookie('inputpassword',password)
                return response
            return redirect('vr_index')
        else:
            if user is None:
                msg = "id/pw incorrect"
            else:
                msg = "Inaccessible"
            return render(request, 'vr_login.html', {'error':msg})
    else:
        return render(request, 'vr_login.html')
    return render(request, 'vr_login.html')

# def vr_login(request):
#     # ohjinjin 함수 전반적으로 수정
#     if request.method == "POST":
#         username = request.POST['ID']
#         password = request.POST['vr_password']
#         user = auth.authenticate(request, username = username, password = password)
#         obj = None
#         msg = ""
#         for eachProf in Profile2.objects.all():
#             if eachProf.user.username == username:
#                 obj = eachProf
#                 break

#         if user is not None and obj is not None:
#             auth.login(request,user)
#             return render(request, 'vr_index.html', {"customedUser":obj})
#         else:
#             if user is None:
#                 msg = "id/pw incorrect"
#             else:
#                 msg = "Inaccessible"
#             return render(request, 'vr_login.html',{'error' : msg})
#     #return render(request, 'accounts/vr_login.html')
#     return render(request, 'vr_login.html') # ohjinjin 문장 추가

"""def vr_signup(request):
    return render(request,'vr_signup.html')"""

    
def logout(request):
    response = render(request,'vr_index.html')
    response.delete_cookie('inputid')
    response.delete_cookie('inputpassword')
    auth.logout(request)
    return redirect('vr_index')

def apply(request):
    return render(request,'apply.html')

def vr_help(request): 
    question =HelpData.objects
    question_list = HelpData.objects.all()
    paginator = Paginator(question_list,10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'vr_help.html',{'question':question,'questions':questions})

def about(request):
    return render(request, 'about.html')

def vr_index(request):  # 추가 chanho - 19_8_2_13:50
    return render(request, 'vr_index.html')

def qna(request):
    return render(request,'qna.html')

def qscreate(request):
    question = HelpData()
    question.question_title = request.GET['question_title']
    question.question_content = request.GET['question_content']
    question.pub_date =timezone.datetime.now()
    question.save()
    return redirect('vr_help')

"""class CreateUserView(CreateView):  # 제네릭의 CreateView는 폼하고 연결돼서, 혹은 모델하고 연결돼서 새로운 데이터를 넣을 때 사용.
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
"""
def question_info(request,question_id):
    question = get_object_or_404(HelpData,id=question_id)
    return render(request,'question_info.html',{'question':question})

def delete(request,question_id):
    question = HelpData.objects.get(id=question_id)
    question.delete()
    return redirect('vr_help')

def modify(request,question_id):
    question = get_object_or_404(HelpData,pk=question_id)
    return render(request,'modify.html',{'question':question})

def qnamodify(request,question_id):
    question = get_object_or_404(HelpData,pk=question_id)
    question.question_title = request.POST['question_title']
    question.question_content = request.POST['question_content']
    question.save()
    return redirect('vr_help')

# def comment_write(request,question_id):
#     if request.method=='POST':
#         question = get_object_or_404(HelpData,pk=question_id)
#         content = request.POST.get('content')
#         if not content:
#             messages.info(request,"You don't write")
#             return redirect('/vr/question_info/'+str(question_id))
#         Comment.objects.create(question=questioin,comment_contents=content)
#         return redirect('/vr/question_info/'+str(question_id))
##
class RegisteredView(TemplateView): # �쉶�썝媛��엯�씠 �셿猷뚮맂 寃쎌슦
    template_name = 'vr_index.html'



class CreateUserView2(CreateView):  # 제네릭의 CreateView는 폼하고 연결돼서, 혹은 모델하고 연결돼서 새로운 데이터를 넣을 때 사용.
    template_name = 'vr_signup.html'     # 회원가입 할 때 띄울 폼 템플릿
    form_class = SignUpForm2
    success_url = reverse_lazy('vr_index') # 성공하면 어디로 갈지, url name
    # 여기서 reverse가 아닌 reverse_lazy를 사용하는 이유: 제네릭뷰 같은경우 타이밍 문제 때문에 reverse_lazy를 사용해야함

    def form_valid(self,form):
        c = {'form':form,}
        user = form.save(commit=False)  #여기서 default User model과 profile이 엮여서 db에 저장되는듯합니다.
        test_record = form.cleaned_data["test_record"]
        sex = form.cleaned_data["sex"]
        birth_date = form.cleaned_data["birth_date"]
        phone_number = form.cleaned_data["phone_number"]
        agreement1 = form.cleaned_data["agreement1"]
        agreement2 = form.cleaned_data["agreement2"]
        
        user.save()

        Profile2.objects.create(user=user, phone_number=phone_number, birth_date = birth_date, test_record=test_record,sex=sex,agreement1=agreement1, agreement2=agreement2)

        return super(CreateUserView2, self).form_valid(form)

def apply_create():
    abook = Wish_Book()
    wbook.title = request.GET['book_name']
    wbook.author = request.GET['book_author']
    wbook.publisher = request.GET['book_publish']
    wbook.pub_date = request.GET['book_year']
    wbook.save()
    return redirect('/ms/ms_index/')