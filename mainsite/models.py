from datetime import datetime
from django.db import models
from datetime import datetime,date
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User #Django預設model
from django.urls import reverse
# from ckeditor.fields import RichTextField
class Post(models.Model):
	pub_title=models.CharField(max_length=200)
	# header_image=models.ImageField()
	title_tag=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	pub_body=models.TextField()
	# category=models.CharField(max_length=255,default='coding')
	slug=models.CharField(max_length=200)
	pub_date=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering =('-pub_date',)
	def __str__(self):#顯示在admin的資料
		return self.pub_title + '|' +str(self.author)
	def get_absolute_url(self):
		return reverse('post_detail',args=(str(self.id))) #新增貼文後導向新增好的貼文的頁面
		# return reverse("index")

class Category(models.Model): #方便以後新增、修改分類
	name=models.CharField(max_length=255)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('/')
# class Comment(models.Model):
# 	post=
class Member(models.Model):
	sex=(
		('F','Female'),
		('M','Male'),
		('O','Other'),
	)
	name=models.CharField(max_length=15)
	sex=models.CharField(max_length=1,choices=sex)
	email=models.EmailField(max_length=50)
	def __str__(self):
		return self.name 
class Profile(models.Model): #Django預設Model.User欄位 user去跟django預設model的User關聯
	user=models.OneToOneField(User,on_delete=models.CASCADE) #on_delete代表的是當對應的類別被刪除之後，這些對應到別人的資料要怎麼被處理，而 CASCADE 就是一倂刪除
	height=models.PositiveIntegerField(default=180)
	male=models.BooleanField(default=False)
	website=models.URLField(null=True)
	def __str__(self):
		return self.user.username

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


