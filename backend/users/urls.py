from django.urls import path
from users import views

urlpatterns = [
    path('', views.LessonView.as_view()),
    path('prof/', views.ProfView.as_view()),
    path('group/', views.GroupView.as_view()),
    path('roomerinno/', views.RoomView.as_view()),
]
#CHANGE: room- -> roomerino
