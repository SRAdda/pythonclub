from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

# Basic forms are already templated
# Forms can be customized

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class MeetingMinutesForm(forms.ModelForm):
    class Meta:
        model=MeetingMinutes
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
