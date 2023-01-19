from django.urls import path
from .views import home, profile, help, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('help/', help, name='users-help'),
]
