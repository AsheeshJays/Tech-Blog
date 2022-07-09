from dataclasses import fields
from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User



class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=('Password'), strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'current-password', 'class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','subject','desc','slug','author','image']
        labels = {'title':'Title','line1':'show Line', 'desc':'Description','image':'Image'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'subject':forms.TextInput(attrs={'class':'form-control'}),
                    'desc':forms.Textarea(attrs={'class':'form-control'}),
                    'slug':forms.TextInput(attrs={'class':'form-control'}),
                    'author':forms.TextInput(attrs={'class':'form-control'}),
        }

class PassForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='New Password confirmtion',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['old password','new password','new password Confirmtion']    