from django.urls import path
from event.views import section


urlpatterns = [
    path('<uuid:pk>/', section.RetrieveUpdateDestroySectionView.as_view()),
]
