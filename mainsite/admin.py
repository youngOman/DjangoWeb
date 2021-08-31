from django.contrib import admin
from .models import Post,Member,Item,User
# Register your models here.
from embed_video.admin import AdminVideoMixin

class Videoadmin(AdminVideoMixin, admin.ModelAdmin):
    pass
class Postadmin(admin.ModelAdmin):
	list_display=('title','slug','pub_date') #COLUMN DISPLAY ON ADMIN

admin.site.register(Post,Postadmin)
admin.site.register(Member)
admin.site.register(Item, Videoadmin)
admin.site.register(User)