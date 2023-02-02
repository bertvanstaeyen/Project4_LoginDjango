from django.urls import path
from . import views
from django.shortcuts import redirect

# This is where the different routes and urls are handled so you get to the right page.
urlpatterns = [
    path('', lambda request: redirect('/day/')),
    path('day/', views.homeDay, name='users-home-day'),
    path('week/', views.homeWeek, name='users-home-week'),
    path('month/', views.homeMonth, name='users-home-month'),
    path('register/', views.RegisterView.as_view(), name='users-register'),
    path('profile/', views.profile, name='users-profile'),
    path('help/', views.help, name='users-help'),
    path('serialNumbers/', views.serialNumber, name='users-serial-number'),
    path('serialNumbers/Delete/<str:id>', views.deleteSerialNumber, name='delete-serial-only'),
    path('serialNumbers/DeleteWithData/<str:id>', views.deleteSerialNumberWithData, name='delete-serial-with-data'),
    path('serialNumbers/updateMeterName/<str:id>', views.updateMeterName, name='update-meter-name')
]
