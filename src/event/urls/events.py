from django.urls import path
from event.views import event, section


urlpatterns = [
    path('', event.ListCreateEventView.as_view()),
    path('<uuid:pk>/', event.RetrieveUpdateDestroyEventView.as_view()),
    path('<uuid:event_id>/sections/', section.ListCreateSectionhView.as_view()),
]
