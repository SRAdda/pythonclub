# Generated by Django 2.1.8 on 2019-05-20 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0008_auto_20190519_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingminutes',
            name='meetingdate',
        ),
    ]
