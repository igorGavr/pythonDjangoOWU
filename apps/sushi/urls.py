from django.urls import path
from .views import SushiListCreateView, SushiRetrieveUpdateDestroyView


urlpatterns = [
    path('', SushiListCreateView.as_view()),
    path('/<int:pk>', SushiRetrieveUpdateDestroyView.as_view())
]