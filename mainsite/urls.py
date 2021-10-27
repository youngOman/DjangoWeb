from django.urls import path,include
from django.contrib import admin
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    # path('authentication/',include([
    #     path('login/', login, name='login'),   
    #     path('',logout,name='logout'),
    #     # path('register/',register,name="register"),
    #     path('accounts/',include('allauth.urls')),  # django-allauth google網址
    # ])),
    path('',HomeView.as_view(),name="home"),
    path('post_detail/<int:pk>/',ArticleDetailView.as_view(),name='post_detail'),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name="Update_Post"), 
    path('add_post/',AddPostView.as_view(),name='addpost'),
    path('post/<int:pk>/remove',DeletePostview.as_view(),name='delete_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>',CategoryView,name="category_page"), #用分類名稱當URL
    path('category_list/',CategoryListView,name="category_list"), #用分類名稱當URL 
    path('userinfo/',userinfo,name='userinfo'),        
    path('video/',video,name='video'),
    path('member/',member,name="member"),
    path('memberdetail/<str:pk>/',memberdetail,name='memberdetail'),

] 