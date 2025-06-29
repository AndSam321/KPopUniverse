from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
