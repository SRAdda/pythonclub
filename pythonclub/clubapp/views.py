from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def gettitles(request):
    title_list=MeetingTitle.objects.all()
    return render(request, 'clubapp/titles.html' ,{'title_list' : title_list})

    
