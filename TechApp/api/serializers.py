from dataclasses import fields
from rest_framework import serializers
from TechApp.models import UserModel, Post, Contact

class UserModelSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ['uid','full_name','username','email','phone','city','password']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','subject','desc','slug','author','date']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','name','email','add','message']