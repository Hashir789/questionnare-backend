from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ImageViewSet

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)
image_router = DefaultRouter()
image_router.register(r'images', ImageViewSet)