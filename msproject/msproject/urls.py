"""msproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#########################################################################
from django.contrib import admin
from django.urls import path, include
import vr_app.views   # ohjinjin 문장 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vr_app.views.index, name="index"), # index.html 파일 생성해뒀습니다. -# ohjinjin 문장 추가
    path('accounts/', include('vr_app.urls')), #2019_07_31_10:45
]
