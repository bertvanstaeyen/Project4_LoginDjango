from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urls for the API
#
# Example
# /api-auth/setData
#
# all urls are admin only
urlpatterns = [
    # get bearer token for authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('setData', views.setData),
    path('getData/<str:pk>', views.getData),
]