from collections import namedtuple
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200)
	slug=models.CharField(max_length=200)
	body=models.TextField()
	pub_date=models.DateTimeField(default=timezone.now)
	class Meta:
		ordering =('-pub_date',)
	def __str__(self):
		return self.title
class Member(models.Model):
	sex=(
		('F','Female'),
		('M','Male'),
		('O','Other'),
	)
	serialnum=models.IntegerField(default='1')	
	name=models.CharField(max_length=15)
	sex=models.CharField(max_length=1,choices=sex)
	email=models.EmailField(max_length=50)
	def __str__(self):
		return self.name #原本會顯示member object加這行則會回傳name的資料
class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
class User(models.Model):
	name=models.CharField(max_length=20,null=False)
	email=models.EmailField(max_length=254)
	password=models.CharField(max_length=20,null=False)
	enabled=models.BooleanField(default=False)
	def __str__(self):
		return self.name