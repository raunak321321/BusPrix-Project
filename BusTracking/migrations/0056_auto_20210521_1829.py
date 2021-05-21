# Generated by Django 3.1.7 on 2021-05-21 12:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0055_auto_20210521_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmultipleroutestickets',
            name='ticketpassenger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BusTracking.passengerticket'),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 21, 12, 59, 18, 532818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 21, 12, 59, 18, 532818, tzinfo=utc)),
        ),
    ]
