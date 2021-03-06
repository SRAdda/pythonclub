from django.test import TestCase
from .models import Meeting, Event, Resource
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from .forms import MeetingForm, EventForm, LessonForm

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

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

class MeetingFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user1', password='P@ssw0rd1')
        
        def test_meetingForm(self):
            form = MeetingForm(
                data={
                    'meetingtitle' : 'meeting1',
                    'meetingdate' : datetime.date(2019,5,30),
                }
            )
            self.assertTrue(form.is_valid)

        def test_meetingFormInvalid(self):
            form = MeetingForm(
                data= {
                    'meetingtitle' : 'meeting1',
                    'meetingdate' : datetime.date(2019,5,30),
                }
            )
            self.assertFalse(form.is_valid())
            
    