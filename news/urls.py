from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('latest/', LatestNewsView.as_view()),
    path('search/', SearchNewsView.as_view()),
    path('save/', SaveArticleView.as_view()),
    path('saved/', SavedArticlesView.as_view()),
]
