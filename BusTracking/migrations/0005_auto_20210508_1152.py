# Generated by Django 3.1.7 on 2021-05-08 06:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0004_auto_20210508_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('query_status', models.CharField(default='Not Completed', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 8, 6, 22, 59, 37066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 8, 6, 22, 59, 37066, tzinfo=utc)),
        ),
    ]
