# Generated by Django 3.1.7 on 2021-05-08 07:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0006_auto_20210508_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='tripDate',
            field=models.DateField(default=datetime.date(2021, 5, 8)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 8, 7, 37, 26, 491953, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 8, 7, 37, 26, 491953, tzinfo=utc)),
        ),
    ]
