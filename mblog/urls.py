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
from mainsite.views import index, logout,video,showpost,memberdetail,member,login,userinfo,addpost,signup,article
from django.views.generic import TemplateView
urlpatterns = [
    path('authentication/',include([
        path('login/', login, name='login'),   
        path('/',logout,name='logout'),
        path('signup/',signup,name="signup"),
        path('accounts/',include('allauth.urls')),  # django-allauth google網址
    ])),
    path('add_post/',addpost,name='addpost'),
    path('article/',article,name='article'),        
    path('admin/', admin.site.urls),
    path('userinfo/',userinfo,name='userinfo'),        
    path('',index),
    path('video/',video),
    path('post/<slug:slug>/',showpost,name='showpost'),
    path('post/<int:year>/<int:month>/<int:day>/<int:postid>/',showpost,name='post-url'), #呼叫views.py的method
    path('member/',member,name="member"),
    path('memberdetail/<str:pk>/',memberdetail,name='memberdetail'),

] 