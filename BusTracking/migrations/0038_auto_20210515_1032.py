# Generated by Django 3.1.7 on 2021-05-15 05:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0037_auto_20210515_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 5, 2, 27, 269788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 5, 2, 27, 269788, tzinfo=utc)),
        ),
    ]
