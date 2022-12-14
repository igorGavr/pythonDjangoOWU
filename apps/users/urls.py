from django.urls import path

from .views import UserCreateView, UserActivateView, UserDeactivateView, UserToAdminView, AdminToUserView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/activate', UserActivateView.as_view()),
    path('/<int:pk>/deactivate', UserDeactivateView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),
]