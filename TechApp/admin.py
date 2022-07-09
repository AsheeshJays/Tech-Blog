from django.contrib import admin
from .models import UserModel, Post, Contact, Comment

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['uid','full_name','username','email','phone','city','otp']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','author','slug','date','image']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','add','message']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['cno','comment_data','user','post','parent','datetime']

