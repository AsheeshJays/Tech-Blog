from django.db import router
from django.urls import path, include
from TechApp.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('PostAPI', views.PostViewset, basename='UserModel'),
router.register('ContactAPI', views.ContactViewset, basename='UserModel')

urlpatterns = [
    path('',include(router.urls)),
]