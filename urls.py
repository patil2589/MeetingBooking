from django.urls import path
from . import views

urlpatterns=[
    path('', views.UserListView.as_view(), name='index'),
    path('book', views.MeetingCreateView.as_view(), name='book'),
    path('meetingSchedule', views.meetingSave, name='meetingSchedule'),
]