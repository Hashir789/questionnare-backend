from django.contrib import admin
from django.urls import path, include, re_path
from gennotate import views
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    re_path('api/signup/', views.signup, name='signup'),
    re_path('api/login/', views.login, name='login'),
    path('userImages/', views.userImages, name='UserImages'),
    path('updateImage/', views.updateImage, name='updateImage'),
    path('createImage/', views.createImage, name='createImage'),
    path('stats/', views.stats, name='stats'),
    path('', hello_world, name='main_page'),
]