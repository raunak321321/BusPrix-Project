from django.contrib import admin

from .models import Bus , Passenger , Tickets , Query , TripDate , Routes , BusStand , BookMultipleRoutesTickets , extenduser , passengerTicket

admin.site.register(Bus)
admin.site.register(Passenger) 
admin.site.register(Tickets) 
admin.site.register(Query) 
admin.site.register(TripDate) 
admin.site.register(Routes) 
admin.site.register(BusStand) 
admin.site.register(BookMultipleRoutesTickets) 
admin.site.register(extenduser) 
admin.site.register(passengerTicket) 