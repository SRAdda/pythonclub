from django.test import TestCase
from .models import Meeting, MeetingMinutes, Event, Resource
from .views import index, meetings, meetingdetail, meetingminutes, events, eventdetail, resources, resourcedetail
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here
class MeetingTest(TestCase):
    def test_stringoutput(self):
        meeting=Meeting(meetingtitle='monthly')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'clubapp_meeting')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='gala')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'clubapp_event')

class TestMeetingMinutes(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingminutes'))
        self.assertEqual(response.status_code, 200)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'attendance')