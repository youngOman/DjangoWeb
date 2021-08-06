from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
def homepage(request):
	posts=Post.objects.all()
	now=datetime.now()
	post_lists=list()
	for count,post in enumerate(posts):
		post_lists.append("NO.{}:".format(str(count))+str(post)+"<hr>")
		post_lists.append("<small>"+str(post.body.encode('utf-8'))+"</small><br><br>")
	return render(request,'index.html',locals())
	
def showpost(request,slug):
	try: 
		post=Post.objects.get(slug=slug)
		if post!=None:
			return render(request,'post.html',locals())
	except:
		return redirect("/")