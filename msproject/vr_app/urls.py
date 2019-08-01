from django.urls import path
from . import views

urlpatterns = [
    path('vr_signup/', views.vr_signup, name='vr_signup'),
    path('vr_login/', views.vr_login, name='vr_login'),
    path('ms_signup/',views.ms_signup,name='ms_signup'),#ohjinjin 문장 수정
    path('logout/',views.logout, name='logout'),
]