# Generated by Django 3.1.7 on 2021-05-15 04:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0016_auto_20210515_1003'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Date',
            new_name='TripDate',
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 34, 2, 740851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 34, 2, 740851, tzinfo=utc)),
        ),
    ]
