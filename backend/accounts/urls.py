from django.urls import path
from accounts import views
#from rest_framework.authtoken import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('login', views.login_view),
    path('api-token-auth/', views.CustomAuthToken.as_view())
    #path('api-token-auth/', views.obtain_auth_token),
]