# Generated by Django 2.1.8 on 2019-05-23 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0012_auto_20190521_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user',
            new_name='user_ID',
        ),
    ]
