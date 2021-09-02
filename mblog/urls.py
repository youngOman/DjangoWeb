"""mblog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib import admin
from mainsite.views import index,video,showpost,memberdata,member_detail,register,logout,login
from django.contrib.auth import views
urlpatterns = [
    path('authentication/',include([
        path('accounts/register/', register, name='register'),
        path('accounts/login/', login, name='login'),   
        path('accounts/logout/', logout, name='logout'),
        path('accounts/', include('allauth.urls'),name="google"),  # django-allauth網址
    ])),
    path('admin/', admin.site.urls),    
    path('',index),
    path('video/',video),
    path('post/<slug:slug>/',showpost),
    path('post/<int:year>/<int:month>/<int:day>/<int:postid>/',showpost,name='post-url'), #呼叫views.py的method
    path('members/',memberdata),
    path('members/<int:serialnum>/',member_detail,name="members"),
     
    
]
    