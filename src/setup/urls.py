from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('person.urls')),
    path('api/events/', include('event.urls.events')),
    path('api/sections/', include('event.urls.sections')),
    path('api/', include('person.auth_urls')),
]
