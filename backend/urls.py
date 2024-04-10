from django.contrib import admin
from django.urls import path, include, re_path
from gennotate import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),
    path('api/get_all_users/', views.get_all_users, name='get_all_users'),
]
