# Generated by Django 2.1.8 on 2019-05-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0005_auto_20190506_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
