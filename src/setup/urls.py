from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('person.urls')),
    path('api/', include('person.auth_urls')),
]
