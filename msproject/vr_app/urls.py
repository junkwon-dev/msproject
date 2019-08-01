from django.urls import path
from . import views

urlpatterns = [
    path('vr_index/', views.index, name = 'vr_index'),
    path('vr_signup/', views.vr_signup, name ='vr_signup'),
    path('vr_login/', views.vr_login, name ='vr_login'),
    path('logout/',views.logout, name='logout'),
    path('apply/', views.apply, name = 'apply'),
    path('help/', views.vr_help, name = 'help'),
    path('about/', views.about, name = 'about'),
]