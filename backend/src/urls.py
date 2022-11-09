from django.urls import path, include

urlpatterns = [
    path('api/', include([
        path('lesson/', include('users.urls')),
        path('accounts/', include('accounts.urls')),
]))
]
