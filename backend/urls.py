from django.contrib import admin
from django.urls import path, include, re_path
from gennotate import views
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    path('api/get_all_users/', views.get_all_users, name='get_all_users'),
    path('', hello_world, name='g'),
]
