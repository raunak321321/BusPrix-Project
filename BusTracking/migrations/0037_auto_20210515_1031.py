# Generated by Django 3.1.7 on 2021-05-15 05:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0036_auto_20210515_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 5, 1, 33, 176350, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 5, 1, 33, 176350, tzinfo=utc)),
        ),
    ]
