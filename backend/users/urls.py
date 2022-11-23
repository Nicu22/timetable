from django.urls import path
from users import views

urlpatterns = [
    path('', views.LessonView.as_view()),
    path('<int:pk>', views.LessonDetailedView.as_view()),
    path('prof/', views.ProfView.as_view()),
    path('prof/<int:pk>', views.ProfDetailedView.as_view()),
    path('group/', views.GroupView.as_view()),
    path('goup/<int:pk>', views.GroupDetailedView.as_view()),
    path('room/', views.RoomView.as_view()),
    path('room/<int:pk>', views.RoomDetailedView.as_view()),
]