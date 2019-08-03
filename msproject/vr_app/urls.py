from django.urls import path
from . import views

urlpatterns = [
    path('vr_signup/', views.CreateUserView.as_view(), name ='vr_signup'),
    path('vr_index/', views.vr_index, name = 'vr_index'), 
    #path('vr_signup/', views.vr_signup, name ='vr_signup'),
    path('vr_login/', views.vr_login, name ='vr_login'),
    path('logout/',views.logout, name='logout'),
    path('apply/', views.apply, name = 'apply'),
    path('vr_help/', views.vr_help, name = 'vr_help'),
    path('about/', views.about, name = 'about'),
    path('qna/',views.qna,name='qna'),
    path('create/',views.create, name='create'),
    path('al/question_infotion/',views.question_info,name='question_info'),
]