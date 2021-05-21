# Generated by Django 3.1.7 on 2021-05-15 04:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0025_auto_20210515_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripDate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_trip', models.DateField(default=datetime.date(2021, 5, 15))),
            ],
        ),
        migrations.DeleteModel(
            name='date',
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 42, 54, 69795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 42, 54, 69795, tzinfo=utc)),
        ),
    ]
