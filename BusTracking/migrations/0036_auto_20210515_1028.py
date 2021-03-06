# Generated by Django 3.1.7 on 2021-05-15 04:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0035_auto_20210515_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='birth_date',
            new_name='tripDate',
        ),
        migrations.AlterField(
            model_name='passenger',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 58, 21, 623485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 15, 4, 58, 21, 623485, tzinfo=utc)),
        ),
    ]
