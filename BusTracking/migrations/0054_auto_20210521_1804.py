# Generated by Django 3.1.7 on 2021-05-21 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0053_auto_20210520_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='passengerTicket',
            fields=[
                ('pass_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('adhaarId', models.BigIntegerField()),
                ('birth_date', models.DateField(default=datetime.date(2021, 5, 21))),
            ],
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 5, 21)),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 5, 21)),
        ),
        migrations.AlterField(
            model_name='query',
            name='QueryDate',
            field=models.DateField(default=datetime.date(2021, 5, 21)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 21, 12, 34, 17, 178704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 21, 12, 34, 17, 178704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripdate',
            name='tripDate',
            field=models.DateField(default=datetime.date(2021, 5, 21)),
        ),
    ]
