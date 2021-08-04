from django.contrib import admin
from .models import Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
	list_display=('title','slug','pub_date') #COLUMN DISPLAY ON ADMIN
	
admin.site.register(Post,Postadmin)
