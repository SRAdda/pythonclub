# Generated by Django 2.1.8 on 2019-05-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0013_auto_20190523_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user_ID',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='event',
            name='eventdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventtime',
            field=models.TimeField(),
        ),
    ]
