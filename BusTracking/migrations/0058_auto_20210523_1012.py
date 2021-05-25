# Generated by Django 3.1.7 on 2021-05-23 04:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BusTracking', '0057_auto_20210521_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 5, 23)),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 5, 23)),
        ),
        migrations.AlterField(
            model_name='passengerticket',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 5, 23)),
        ),
        migrations.AlterField(
            model_name='query',
            name='QueryDate',
            field=models.DateField(default=datetime.date(2021, 5, 23)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='destinationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 23, 4, 42, 57, 556112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='routes',
            name='stationTime',
            field=models.TimeField(default=datetime.datetime(2021, 5, 23, 4, 42, 57, 556112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tripdate',
            name='tripDate',
            field=models.DateField(default=datetime.date(2021, 5, 23)),
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noOfSeatsBooked', models.IntegerField(default=0)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusTracking.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusTracking.routes')),
                ('tripdate', models.ForeignKey(default=datetime.date(2021, 5, 23), on_delete=django.db.models.deletion.CASCADE, to='BusTracking.tripdate')),
            ],
        ),
    ]
