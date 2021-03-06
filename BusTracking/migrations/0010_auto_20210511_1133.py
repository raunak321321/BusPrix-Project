# Generated by Django 3.1.7 on 2021-05-11 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0009_auto_20210510_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='tripDate',
            field=models.DateField(default=datetime.date(2021, 5, 11)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 11, 6, 3, 46, 40632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 11, 6, 3, 46, 40632, tzinfo=utc)),
        ),
    ]
