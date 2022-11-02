from django.urls import path
from users import views

urlpatterns = [
    path('', views.LessonView.as_view()),
    path('prof/', views.ProfView.as_view()),
    path('group/', views.GroupView.as_view()),
    path('room/', views.RoomView.as_view()),
]