from django.urls import path
from .views import homeDay, homeWeek, homeMonth, profile, help, RegisterView, serialNumber
from django.shortcuts import redirect

# This is where the different routes and urls are handled so you get to the right page.
urlpatterns = [
    path('', lambda request: redirect('/day/')),
    path('day/', homeDay, name='users-home-day'),
    path('week/', homeWeek, name='users-home-week'),
    path('month/', homeMonth, name='users-home-month'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('help/', help, name='users-help'),
    path('serialNumbers/', serialNumber, name='users-serial-number'),
]
