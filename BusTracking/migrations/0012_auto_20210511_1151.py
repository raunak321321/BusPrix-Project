# Generated by Django 3.1.7 on 2021-05-11 06:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0011_auto_20210511_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 11, 6, 21, 41, 760640, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 11, 6, 21, 41, 760640, tzinfo=utc)),
        ),
    ]
