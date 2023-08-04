from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('api/list/data',BathHouseView.as_view()),
    path('api/v1/data/delete/<int:pk>/',BathHouseDeleteView.as_view()),
    path('api/v1/data/update/<int:pk>/',BathHouseUpdateView.as_view()),
    path('api/search/',SearchBathHouse.as_view()),
    path('api/filter/',BathHouseFiltter.as_view()),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'), 
]