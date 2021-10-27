from django.contrib import admin
from .models import Post,Member,Item,Profile,Category
# Register your models here.
from embed_video.admin import AdminVideoMixin

class Postadmin(admin.ModelAdmin):
	list_display=('pub_title','slug','pub_date') #COLUMN DISPLAY ON ADMIN
class Videoadmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Post,Postadmin)
admin.site.register(Item,Videoadmin)
admin.site.register(Member)
admin.site.register(Profile)
admin.site.register(Category)

