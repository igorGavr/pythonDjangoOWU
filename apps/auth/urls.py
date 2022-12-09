from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ActivateUserView
from django.urls import path

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view())

]