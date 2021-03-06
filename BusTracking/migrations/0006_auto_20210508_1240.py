# Generated by Django 3.1.7 on 2021-05-08 07:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0005_auto_20210508_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RoutesD', to='BusTracking.busstand'),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 8, 7, 10, 11, 590223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RoutesO', to='BusTracking.busstand'),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 8, 7, 10, 11, 590223, tzinfo=utc)),
        ),
    ]
