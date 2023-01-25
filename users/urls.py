from django.urls import path
from .views import homeDay, homeWeek, homeMonth, profile, help, RegisterView
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/day/')),
    path('day/', homeDay, name='users-home-day'),
    path('week/', homeWeek, name='users-home-week'),
    path('month/', homeMonth, name='users-home-month'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('help/', help, name='users-help'),
]
