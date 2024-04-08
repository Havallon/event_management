from django.urls import path
from event.views import event


urlpatterns = [
    path('', event.ListCreateEventView.as_view()),
    path('<uuid:pk>/', event.RetrieveUpdateDestroyEventView.as_view()),
]
