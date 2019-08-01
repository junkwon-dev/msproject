from django.urls import path
from . import views

urlpatterns = [
    path('ms_signup/', views.CreateUserView.as_view(), name ='ms_signup'),
    path('ms_login/', views.ms_login, name ='ms_login'),
    path('list/', views.list, name = 'list'),
    path('ms_index/', views.ms_index, name = 'ms_index'),
    path('ms_library', views.ms_library, name = 'ms_library'),
]