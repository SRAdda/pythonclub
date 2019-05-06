from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def gettitles(request):
    titles_list=Meeting.objects.all()
    return render(request, 'clubapp/titles.html' ,{'titles_list' : titles_list})

def getevents(request):
    events_list=Event.objects.all()
    return render(request, 'clubapp/events.html', {'events_list': events_list})    

def eventdetail(request, id):
    detail=get_object_or_404(Event, pk=id)
    context={ 'details' : details, }
    return render(request, 'clubapp/eventdetail.html', context=context)

def getresources(request, id):
    resources_list=Resources.objects.all()
    return render(request, 'clubapp/resources.html', {'resources_list': resources_list})