# Generated by Django 3.1.7 on 2021-05-15 04:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0027_auto_20210515_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='age',
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 44, 38, 242904, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 44, 38, 242904, tzinfo=utc)),
        ),
    ]