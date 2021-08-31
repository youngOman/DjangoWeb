from django.shortcuts import redirect,render
from django.http import Http404
from .models import Post,Member,Item,User
from django.contrib.auth.forms import UserCreationForm
from .forms import Loginform
# Create your views here.
def index(request):
	if 'useraccount' in request.session:
		useraccount=request.session['account'] #取出
		useremail=request.session['email'] 
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
def memberdata(request):
	try:
		path = request.get_host()
		members=Member.objects.all() #取得會員資料
		if members!=None:
			return render(request,'member.html',locals())
	except Member.DoesNotExist:
		raise Http404('找不到指定編號')  #raise手動設定一個異常
def member_detail(request,serialnum): 
	try:
		m=Member.objects.filter(serialnum=serialnum)
	except Member.DoesNotExist:
		raise Http404('找不到指定編號')
	return render(request,'memberdata.html',locals())
def register(request): #註冊
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors:", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {
			'form': form
		}
		return render(request, 'register.html', context)
def login(request):
	if request.method == 'POST':
		login_form=Loginform(request.POST) 
		if login_form.is_valid():	 #檢查是否輸入正確		
			useraccount=request.POST['account'].strip() #去掉前後空白
			userpassword=request.POST['password'] #使用者輸入由POST傳進來的
			message='登入成功'
		try: # 用try是因為真的找不到useraccount的話避免中斷網站程式
			user=User.objects.get(name=useraccount)
			if user.password == userpassword:
				request.session['account']=user.name #使用者的Name
				request.session['email']=user.email
				return redirect('/')
			else:
				message='密碼錯誤'
		except:
			message='無此使用者'
		else:
			message='帳號或密碼錯誤'
			
	else:
		login_form=Loginform() #若不是POST，產生一個新的表單
	return render(request,'login.html',locals())
def logout(request):
	request.session['account']=None
	return render(request,'logout.html',locals())