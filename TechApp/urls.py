from django.urls import path
from TechApp import views

urlpatterns = [
    path('',views.HomePage,name='homePage'),
    path('blogpost/<str:slug>/',views.BlogPost,name='blogpost'),
    path('aboutPage/',views.AboutPage,name='aboutPage'),
    path('dashboardPage/',views.DashboardPage,name='dashboardPage'),
    path('signupPage/',views.SignUpPage,name='signupPage'),
    path('loginPage/',views.LoginPage,name='loginPage'),
    path('logoutPage/',views.LogoutPage,name='logoutPage'),
    path('search/',views.Search,name='search'),
    path('addPost/', views.AddPost,name='addpost'),
    path('editpost/<int:id>/', views.EditPost,name='editpost'),
    path('contact/',views.ContactPage,name="contact"),
    path('deletepost/<int:id>/', views.Delete_Post,name='deletepost'),
    path('changepassword/', views.ChangePassword, name='changepassword'),
    path('forgetpassword/',views.ForgetPasswordPage,name='forgetpassword'),
    path('enterotp/<str:username>/',views.enterotp,name='enterotp'),
    path('resetpassword/<str:username>/',views.resetPassword,name='resetpassword'),
    path('postComment/',views.Comments,name='postComment'),
]
