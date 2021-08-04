from django.shortcuts import render
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
