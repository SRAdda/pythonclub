from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.http import HttpResponseNotModified
from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def meetings(request):
    meetings=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html' , {'meetings': meetings})

def meetingminutes(request):
    meetingminutes=MeetingMinutes.objects.all()
    return render(request, 'clubapp/meetingminutes.html' , {'meetingminutes': meetingminutes})


def meetingdetail(request, id):
    meetingdetail=get_object_or_404(Meeting, pk=id)
    return render(request, 'clubapp/meetingdetail.html', {'meeting' : meeting})

def events(request):
    events_list=Event.objects.all()
    return render(request, 'clubapp/events.html', {'events_list': events_list})    

def eventdetail(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'clubapp/eventdetail.html', {'event' : event})

def resources(request):
    resources_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html', {'resources_list': resources_list})

def resourcedetail(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'clubapp/resourcedetail.html', {'resource' : resource})
