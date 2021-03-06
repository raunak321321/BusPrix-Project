# Generated by Django 3.1.7 on 2021-05-07 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('bus_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=50)),
                ('noOfSeats', models.IntegerField()),
                ('busConductor', models.CharField(max_length=50)),
                ('conductorPhone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('pass_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('adhaarId', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusTracking.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('stationTime', models.TimeField()),
                ('destinationTime', models.TimeField()),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusTracking.routes')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('pass_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusTracking.passenger')),
                ('schedules_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusTracking.schedules')),
            ],
        ),
    ]
