from datetime import datetime
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User #Django預設model
from django.urls import reverse
class Post(models.Model):
	title=models.CharField(max_length=200)
	slug=models.CharField(max_length=200)
	body=models.TextField()
	pub_date=models.DateTimeField(default=timezone.now)
	class Meta:
		ordering =('-pub_date',)
	def __str__(self):#顯示在admin的資料
		return self.title
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
class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
class Profile(models.Model): #Django預設Model.User欄位 user去跟django預設model的User關聯
	user=models.OneToOneField(User,on_delete=models.CASCADE) #on_delete代表的是當對應的類別被刪除之後，這些對應到別人的資料要怎麼被處理，而 CASCADE 就是一倂刪除
	height=models.PositiveIntegerField(default=180)
	male=models.BooleanField(default=False)
	website=models.URLField(null=True)
	def __str__(self):
		return self.user.username
class MemberPost(models.Model):
	pub_name=models.ForeignKey(User,on_delete=models.CASCADE)
	pub_title=models.CharField(max_length=25)
	pub_body=models.TextField()
	pub_date=models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.pub_title
