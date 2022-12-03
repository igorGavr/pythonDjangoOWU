from django.urls import path

from .views import AutoParkListView, CarListCreateView

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>/cars', CarListCreateView.as_view())
]