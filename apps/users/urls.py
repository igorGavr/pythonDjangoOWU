from django.urls import path

from .views import UserCreateView, UserToAdminView, UserActivateView, AdminToUserView, UserDeactivateView, AutoParkListCreateView, AddAvatarView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/auto_parks', AutoParkListCreateView.as_view()),
    path('/avatar', AddAvatarView.as_view()),
    path('/<int:pk>/activate', UserActivateView.as_view()),
    path('/<int:pk>/deactivate', UserDeactivateView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),
]
