# Generated by Django 3.1.7 on 2021-06-05 12:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0062_auto_20210605_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 6, 5, 12, 45, 16, 913928, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 6, 5, 12, 45, 16, 913928, tzinfo=utc)),
        ),
    ]
