from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('gettitles/', views.gettitles, name='titles'),
    path('getevents/', views.getevents, name='events'),
    path('details/<int:id>', views.eventdetail, name='eventdetail'),
    path('getresources/', views.getresources, name='resources'),

]
