from django.contrib.messages.api import success
from django.forms import fields
from django.shortcuts import redirect,render
from django.http import Http404,request
from django.views.generic.edit import CreateView
from .models import *
from .forms import Loginform,Userregisterform,Postform,EditForm
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import  reverse_lazy
# Create your views here.
# @login_required(login_url='/authentication/login/') #若沒登入就想進入test.html會被強制導回Login
class HomeView(ListView):
	model=Post
	template_name="index.html"
	cats=Category.objects.all()
	ordering=['-pub_date']
	def get_context_data(self,*args,**kwargs): #要在不同頁面也能看到下拉式選單的話需在每個View加上這段
		category_menu=Category.objects.all()
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		context["category_menu"] = category_menu
		return context
class ArticleDetailView(DetailView):
	model=Post
	template_name='post_detail.html'
class AddPostView(CreateView):
	model=Post
	form_class=Postform
	template_name='addpost.html'
	# fields='__all__' 
class UpdatePostView(UpdateView): #as_view的寫法
	model=Post
	form_class=EditForm
	template_name='update_post.html'
class DeletePostview(DeleteView):
	model=Post
	template_name='delete_post.html'
	success_url=reverse_lazy('home')
class AddCategoryView(CreateView):
	model=Category
	template_name='add_category.html'
	fields='__all__'
def CategoryListView(request): #cats是由Model.Post的category傳遞參數給cats當URL
	Category_MenuList=Category.objects.all() #用分類名稱當URL
	return render(request,'category_list.html',{'Category_MenuList':Category_MenuList}) #傳送context至html

def CategoryView(request,cats): #cats是由Model.Post的category傳遞參數給cats當URL
	Category_posts=Post.objects.filter(category=cats) #用分類名稱當URL
	return render(request,'category.html',{'cats':cats,'Category_posts':Category_posts}) #傳送context至html
	

def video(request):
	obj=Item.objects.all() #Item=videos
	return render(request,'index.html',locals())
def member(request):
	if request.user.is_authenticated:
		username=request.user.username	
	try:
		path = request.get_host()
		members=Member.objects.all() #取得會員資料
		if members!=None:
			return render(request,'member.html',locals())
	except Member.DoesNotExist:
		raise Http404('找不到指定編號')  #raise手動設定一個異常
def memberdetail(request,pk):
	try:
		members=Member.objects.filter(id=pk)
	except Member.DoesNotExist:
		raise Http404('找不到指定編號')
	return render(request,'memberdetail.html',locals())
def userinfo(request):
	if request.user.is_authenticated:
		username=request.user.username
		try:
			user=User.objects.get(username=username)
			userinfo=Profile.objects.get(user=user)
		except:
			pass
	return render(request,'userinfo.html',locals())




