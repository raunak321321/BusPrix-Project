from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
class Bus(models.Model):
    bus_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    Type = models.CharField(max_length = 50)
    noOfSeats = models.IntegerField()
    busConductor = models.CharField(max_length=50)
    conductorPhone = models.CharField(max_length=20)
    image = models.ImageField(default="BusTracking/images/image1.webp")

    def __str__(self):
        return self.name


class Passenger(models.Model):
    pass_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length =100)
    adhaarId = models.BigIntegerField()
    birth_date = models.DateField(default=date.today())

    def __str__(self):
        return " ".join([str(self.pass_id),self.name])


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key = True)
    passenger = models.ForeignKey('Passenger',on_delete=models.CASCADE)
    routes = models.ForeignKey('Routes',on_delete=models.CASCADE,default=1)
    trip = models.ForeignKey('TripDate',on_delete=models.CASCADE,default=1)
    ticketpassenger = models.ForeignKey("passengerTicket",on_delete=models.CASCADE,default=1)

    def __str__(self):
        return " ".join([str(self.routes.route_id),str(self.ticket_id),str(self.trip.trip_id),str(self.ticketpassenger.pass_id)])

class BusStand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 100)
    bus = models.ForeignKey('Bus',on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return " ".join([self.name,str(self.id)])

class Routes(models.Model):
    route_id = models.AutoField(primary_key = True)
    origin = models.ForeignKey('BusStand',on_delete=models.CASCADE,related_name="RoutesO",)
    destination = models.ForeignKey('BusStand',on_delete=models.CASCADE,related_name="RoutesD",)
    bus = models.ForeignKey('Bus',on_delete=models.CASCADE)
    stationTime = models.TimeField(default=timezone.now())
    destinationTime = models.TimeField(default=timezone.now())
    cost = models.IntegerField(default=500)

    def __str__(self):
        return " ".join([str(self.origin.id),str(self.destination.id),str(self.bus.bus_id),str(self.route_id),str(self.cost),str(self.stationTime),str(self.destinationTime)])

class Query(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500,default="")
    query_status = models.CharField(max_length=20,default="Not Completed")
    QueryDate = models.DateField(default=date.today())

    def __str__(self):
        return self.name

class BookMultipleRoutesTickets(models.Model):
    routeOrigin = models.ForeignKey('Routes',on_delete=models.CASCADE,related_name="ORoutes",default=5)
    routeDestination = models.ForeignKey('Routes',on_delete=models.CASCADE,related_name="DRoutes",default=6)
    cost = models.IntegerField(default=1000)
    ticket_id = models.AutoField(primary_key = True)
    passenger = models.ForeignKey('Passenger',on_delete=models.CASCADE)
    routes = models.CharField(max_length =20)
    trip = models.ForeignKey('TripDate',on_delete=models.CASCADE,default=1)
    ticketpassenger = models.ForeignKey("passengerTicket",on_delete=models.CASCADE,default=1)

    def __str__(self):
        return " ".join([str(self.ticket_id),str(self.trip.trip_id),str(self.cost),str(self.routeOrigin.route_id),str(self.routeDestination.route_id),str(self.ticketpassenger.pass_id)])

class TripDate(models.Model):
    trip_id = models.AutoField(primary_key = True)
    tripDate = models.DateField(default=date.today())

    def __str__(self):
        return str(self.trip_id)


class extenduser(models.Model):
    adhaarId = models.BigIntegerField()
    birth_date = models.DateField(default=date.today())
    pass_id  = models.IntegerField(default=1)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return " ".join([str(self.pass_id),str(self.birth_date),str(self.adhaarId)])

class passengerTicket(models.Model):
    pass_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length =100)
    adhaarId = models.BigIntegerField()
    birth_date = models.DateField(default=date.today())

    def __str__(self):
        return " ".join([str(self.pass_id),self.name])

class Seats(models.Model):
    noOfSeatsBooked = models.IntegerField(default=0)
    route = models.ForeignKey("Routes",on_delete=models.CASCADE)
    tripdate = models.DateField(default=date.today())

    def __str__(self):
        return str(self.noOfSeatsBooked)

# the main thing in seats models is that we have to create seats columns for all bus and routes there is no need to put any tripdate as it is defalut to today date 




# jb bandha apne time ka schedule dega tb use schedule id bhi milegi