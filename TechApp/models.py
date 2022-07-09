from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserModel(models.Model):
    uid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone  = models.CharField(max_length=15,default=None,null=True,blank=True)
    city = models.CharField(max_length=255,default=None,null=True,blank=True)
    otp = models.IntegerField(default=0,blank=True,null=True)


class Post(models.Model):
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    desc = models.TextField()
    slug = models.CharField(max_length=150,unique=True)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    add = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    comment_data = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment_data[0:13] + "..." + "by " + self.user.username

    
