from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('getevents/', views.getevents, name='events'),
    path('eventdetails/<int:id>', views.eventdetails, name='eventdetails'),
    path('resources/', views.resources, name='resources'),
    path('resourcedetail/<int:id>', views.resourcedetail, name='resourcedetail'),
    
]
