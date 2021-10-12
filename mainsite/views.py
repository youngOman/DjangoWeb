from django.shortcuts import redirect,render
from django.http import Http404,request
from .models import *
from .forms import Loginform,MemberPostform,Usersignupform
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/authentication/login/') #若沒登入就想進入test.html會被強制導回Login
def index(request,pid=None,del_pass=None):
	if request.user.is_authenticated:
		username=request.user.username
		posts=Post.objects.all()
		return render(request,'index.html',locals()) #locals會把所有區域變數使用字典型態打包起來
def video(request):
	obj=Item.objects.all() #Item=videos
	return render(request,'index.html',locals())
def showpost(request,slug):
	try: 
		post=Post.objects.get(slug=slug)
		if post!=None:
			return render(request,'post.html',locals())
	except:
		return redirect("/")
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
# def login(request): #SESSION的寫法
# 	if request.method == 'POST':
# 		login_form=Loginform(request.POST) 
# 		if login_form.is_valid():	 #檢查是否輸入正確		
# 			login_name=request.POST['account'].strip() #去掉前後空白
# 			login_password=request.POST['password'] #使用者輸入由POST傳進來的
# 			try: # 若找不到useraccount的話避免中斷網站程式
# 				user=MyUser.objects.get(name=login_name)
# 				if user.password == login_password:
# 					request.session['account']=user.name #使用者的Name
# 					request.session['email']=user.email
# 					messages.add_message(request,messages.SUCCESS,"成功登入")
# 					return redirect('/')
# 				else:
# 					messages.add_message(request,messages.WARNING,"密碼錯誤")
# 			except:
# 				messages.add_message(request,messages.WARNING,"無此使用者")
# 		else:
# 			messages.add_message(request,messages.INFO,"請檢查欄位")

# 	else:
# 		login_form=Loginform() #若不是POST，產生一個新的表單
# 	return render(request,'authentication/login.html',locals())
def login(request): #auth的寫法 
	if request.user.is_authenticated: 
		return redirect("/")
	else:
		if request.method == 'POST':
			login_form=Loginform(request.POST) 
			if login_form.is_valid():	 #檢查是否輸入正確		
				login_name=request.POST['account'].strip() #去掉前後空白
				login_password=request.POST['password'] #使用者輸入由POST傳進來的
				user=auth.authenticate(username=login_name,password=login_password) 
				if user is not None:
					if user.is_active:
						auth.login(request,user)
						messages.add_message(request,messages.SUCCESS,"成功登入")
						return redirect('/')
					else:
						messages.add_message(request,messages.WARNING,"帳號尚未啟用")
				else:
					messages.add_message(request,messages.WARNING,"帳號或是密碼錯誤:(")
			else:
				messages.info(request,messages.INFO,"請檢查欄位")
		else:
			login_form=Loginform() # 若不是POST，產生一個新的表單instance
		return render(request,'authentication/login.html',locals())
def logout(request):
	auth.logout(request)
	messages.add_message(request,messages.INFO,"已登出")
	return redirect("/")
def signup(request):
	if request.user.is_authenticated: #如果使用者已經登入又想進入登入頁面就導回首頁
		return redirect("/")
	else:
		if request.method == 'POST':
			form=Usersignupform(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username') #字典會提供給我們(通過驗證的欄位)的數據
				messages.success(request,user+'成為了全婆幫會員o(^▽^)o')
			context={'form':form}
		else: 
			form=Usersignupform()
		return render(request,"authentication/signup.html",locals())
def userinfo(request):
	if request.user.is_authenticated:
		username=request.user.username
		try:
			user=User.objects.get(username=username)
			userinfo=Profile.objects.get(user=user)
		except:
			pass
	return render(request,'userinfo.html',locals())
def article(request):
	if request.user.is_authenticated:
		username=request.user.username
		useremail=request.user.email
		try:
			pub_name=User.objects.get(username=username)
			addposts=MemberPost.objects.filter(pub_name=pub_name)
		except:
			pass
	messages.get_messages(request)		
	return render(request,"article.html",locals())
@login_required(login_url='/authentication/login/') #若沒登入就想進入test.html會被強制導回Login
def addpost(request):
	username=request.user.username
	useremail=request.user.email
	messages.get_messages(request)
	if request.method =='POST':
		pub_name=User.objects.get(username=username)
		post=MemberPost(pub_name=pub_name)
		post_form=MemberPostform(request.POST,instance=post) #從使用者那獲取user傳回MemberPostform結合，才有user的資料
		if post_form.is_valid():
			messages.add_message(request,messages.INFO,"發文成功 ༼ つ◕(oo)◕༽つ")
			post_form.save()
			return redirect("article")
		else:
			messages.add_message(request,messages.INFO,"欄位填寫不完全")
	else:
		post_form=MemberPostform()
	return render(request,'addpost.html',locals())