# Generated by Django 3.1.7 on 2021-05-15 04:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0022_auto_20210515_1008'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TripDate',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 39, 27, 9899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 39, 27, 9899, tzinfo=utc)),
        ),
    ]
