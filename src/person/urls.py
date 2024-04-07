from django.urls import path
from person import views


urlpatterns = [
    path('', views.ListCreatePersonView.as_view()),
]
