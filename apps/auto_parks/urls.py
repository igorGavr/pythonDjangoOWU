from django.urls import path

from .views import AutoParkListCreateView, CarListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', CarListCreateView.as_view())
]