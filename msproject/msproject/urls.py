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
import ms_app.views   # ohjinjin 문장 추가
from django.conf import settings # 추가 chanho - 19_8_1_19:50
from django.conf.urls.static import static # 추가 chanho - 19_8_1_19:50

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vr_app.views.index, name="index"), # index.html 파일 생성해뒀습니다. -# ohjinjin 문장 추가
    path('vr/', include('vr_app.urls')), #2019_07_31_10:45, ohjinjin 수정 2019_08_01 14:57
    path('ms/', include('ms_app.urls')), # ohjinjin 문장 추가
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 추가 chanho - 19_8_1_19:50
