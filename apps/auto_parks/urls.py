from django.urls import path

from .views import AutoParkListView, AddCarToAutoParkView

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view())
]