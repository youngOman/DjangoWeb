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
from mainsite.views import index,UpdatePostView,ArticleDetailView,AddPostView,DeletePostview,logout,video,memberdetail,member,login,userinfo,register   #article
from django.views.generic import TemplateView
urlpatterns = [
    path('authentication/',include([
        path('login/', login, name='login'),   
        path('',logout,name='logout'),
        path('register/',register,name="register"),
        path('accounts/',include('allauth.urls')),  # django-allauth google網址
    ])),
    # path('article/',article,name='article'),
    path('',index),
    path('post_detail/<int:pk>/',ArticleDetailView.as_view(),name='post_detail'),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name="Update_Post"), 
    path('add_post/',AddPostView.as_view(),name='addpost'),
    path('post/<int:pk>/remove',DeletePostview.as_view(),name='delete_post'),
    path('admin/', admin.site.urls),
    path('userinfo/',userinfo,name='userinfo'),        
    path('video/',video),
    path('member/',member,name="member"),
    path('memberdetail/<str:pk>/',memberdetail,name='memberdetail'),

] 