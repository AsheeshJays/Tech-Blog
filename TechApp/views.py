from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import UserModel,Post, Contact,Comment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserLoginForm,PostForm, PassForm
from django.core.mail import send_mail,send_mass_mail
from random import randint
from TechApp.templatetags import extras


def HomePage(request):
    post = Post.objects.all()
    return render(request, 'homepage.html',{'Post':post})

def BlogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comment = Comment.objects.filter(post=post, parent=None)
    replies= Comment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.cno not in replyDict.keys():
            replyDict[reply.parent.cno]=[reply]
        else:
            replyDict[reply.parent.cno].append(reply)
    return render(request, 'singleblog.html',{'P':post,'C':comment,'replyDict': replyDict})

def Comments(request):
    if request.method == 'POST':
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(id=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            c = Comment(comment_data=comment, user=user,post=post)
            c.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= Comment.objects.get(cno=parentSno)
            c=Comment(comment_data= comment, user=user, post=post , parent=parent)
            c.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/blogpost/{post.slug}/")

def AboutPage(request):
    return render(request, 'aboutpage.html')

def DashboardPage(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        post_user = Post.objects.filter(user=user)
        return render(request, 'dashboardpage.html',{'post':post_user,'user':user})
    else:
        return HttpResponseRedirect('/loginPage/')

def SignUpPage(request):
    if request.method == 'POST':
        u = UserModel()
        u.full_name = request.POST.get("full_name")
        uname = u.username = request.POST.get("username")
        pward = request.POST.get("password")
        u.email = request.POST.get("email")
        u.phone = request.POST.get("phone")
        u.city = request.POST.get("city")
        user = User.objects.create_user(username=uname,password=pward)
        u.save()
        messages.success(request, 'You Account Created Successfully ')
    return render(request, 'signuppage.html')

def LoginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserLoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboardPage/')
            else:
                messages.success(request, "Your Username & Password does'nt match!!!" )
        else:
            fm = UserLoginForm()
        return render(request, 'loginpage.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboardPage/')

def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')

def Search(request):
    query = request.GET['query']
    if len(query)>50:
        allPost = []
    else:
        allPost = Post.objects.filter(title__icontains=query)

    if allPost.count() == 0:
        messages.error(request, 'No Search Result Found Please Refine  Your Query')
    return render(request, 'search.html',{'Post':allPost,'query':query})

def AddPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST, request.FILES)
            if fm.is_valid():
                user = request.user
                title = fm.cleaned_data['title']
                subject = fm.cleaned_data['subject']
                desc = fm.cleaned_data['desc']
                slug = fm.cleaned_data['slug']
                author = fm.cleaned_data['author']
                image = fm.cleaned_data['image']
                pst = Post(title=title, desc=desc,subject=subject,slug=slug,author=author,image=image,user=user)
                pst.save()
                messages.success(request, 'your blog posted Successfully!!')
            else:
                messages.warning(request, "Not Posted blog Please try once again!!!")
        else:
            fm = PostForm()
        return render(request, 'addpost.html',{'form':fm})  
    else:
        return HttpResponseRedirect('/loginPage/')

def EditPost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, request.FILES, instance=pi)
            if fm.is_valid():
                messages.success(request, 'Your Post Update Successfully!!!')
                fm.save()
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        return render(request, 'editpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/loginPage/')

def ContactPage(request):
    if request.method == 'POST':
        c = Contact()
        c.name = request.POST.get('name')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.message = request.POST.get('message')
        subject = "For Contact"
        body =  """
                    Hello!!!!
                    Thanks For Beleving us .
                    Me & My Team   will conact
                    very Soon 

                    Team:  Tech-Blog
                """
        send_mail(subject, body,"armannmalik9880@gmail.com",[c.email,], fail_silently=False)
        c.save()
        messages.success(request, 'Thank You for contact us')
    return render(request, 'contact.html')

def Delete_Post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboardPage/')
    else:
        return HttpResponseRedirect('/loginPage/')

def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PassForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                
                return HttpResponseRedirect('/dashboardPage/')
        else:
            form = PassForm(user=request.user)

        return render(request, 'changepassword.html',{'form':form})
    else:
        return HttpResponseRedirect('/loginPage/')

def ForgetPasswordPage(request):
    if(request.method=="POST"):
        flag = False
        username = request.POST.get("username")
        user = UserModel.objects.get(username=username)
        flag=True
        if(flag==True):
            user.otp = randint(1000,9999)
            user.save()
            subject = "OTP for Password Reset"
            body =  """
                        Hello!!!!
                        Your OTP for PasssWord Rest is
                        {}
                        Team:   Tech-Blog
                    """.format(user.otp)
            send_mail(subject, body,"armannmalik9880@gmail.com",[user.email,], fail_silently=False)
            return HttpResponseRedirect('/enterotp/'+username+"/")
        else:
            messages.error(request,"User Name not fund")
    return render(request, 'forgetpassword.html')
def enterotp(request,username):
    if(request.method=="POST"):
        flag = False
        otp = int(request.POST.get("otp"))
        user = UserModel.objects.get(username=username)
        flag=True
        if(flag==True):
            if(user.otp==otp):
                return HttpResponseRedirect('/resetpassword/'+username+"/")
            else:
                messages.error(request,"OTP Does't Match")    
        else:
            messages.error(request,"User Name not fund")
    return render(request, 'enterotp.html')

def resetPassword(request,username):
    if(request.method=="POST"):
        password1 = request.POST.get("p1")
        password2 = request.POST.get("p2")
        # try:
        user = User.objects.get(username=username)
        if(password1==password2):
            user.set_password(password1)
            user.save()
            subject = "Password Reset"
            body =  """
                       Your Password Reset
                       successfully.New 
                       password genereted
                        
                        Team:  Tech-Blog
                    """
            send_mail(subject, body,"armannmalik9880@gmail.com",[user.email,], fail_silently=False)
            return HttpResponseRedirect('/loginPage/')
        else:
            messages.error("Password and Confirm Password not Match")
        # except:
        #     messages.error(request,"User not fund")
    return render(request,"resetpassword.html")


