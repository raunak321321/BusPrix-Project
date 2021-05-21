from django.shortcuts import render , redirect
from django.http import HttpResponse 
from math import ceil
from .models import Tickets , Passenger , Query , Routes , BusStand , Bus ,extenduser ,TripDate , BookMultipleRoutesTickets , passengerTicket
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import sys


# Create your views here.
def index(request):
    busstand = BusStand.objects.values('name')
    bus = Bus.objects.all()
    n = len(bus)
    n_slides = n//2 + ceil((n/2)-(n//2))
    return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand})

def ticketchecker(request,myid):

    busstand = BusStand.objects.values('name')
    try:
            ticket = Tickets.objects.filter(passenger=myid)
            ticket2 = BookMultipleRoutesTickets.objects.filter(passenger=myid)
            if(len(ticket)>0 or len(ticket2)>0):
                passenger = Passenger.objects.filter(pass_id=myid)
                a = len(ticket) + len(ticket2)
                n_slides = a//2 + ceil((a/2)-(a//2))
                output=[]
                output1=[]

                
                if len(ticket)>0:
                    allstrticket=[]
                    allarrticket=[]
                    allroutes=[]
                    allstrroutes=[]
                    allarrroutes=[]
                    allbusstandOrigin=[]
                    allbusstandDestination=[]
                    allbus=[]
                    for item in ticket:
                        anything={}
                        strticket = str(item)
                        anything["strticket"]=strticket
                        arrticket = strticket.split()
                        anything["arrticket"]=arrticket
                        routes = Routes.objects.filter(route_id = int(arrticket[0]))
                        pass_ticket = passengerTicket.objects.filter(pass_id = int(arrticket[3])).values('name','birth_date','adhaarId')
                        anything["pass_ticket"]=pass_ticket
                        trip = TripDate.objects.filter(trip_id = int(arrticket[2])).values('tripDate')
                        anything["routes"]=routes
                        anything["trip"]=trip
                        strroutes = str(routes[0])
                        anything["strroutes"]=strroutes
                        arrroutes = strroutes.split()
                        anything["arrroutes"]=arrroutes
                        busstandOrigin = BusStand.objects.filter(id = int(arrroutes[0]))
                        busstandDestination = BusStand.objects.filter(id = int(arrroutes[1]))
                        anything["busstandOrigin"]=busstandOrigin
                        anything["busstandDestination"]=busstandDestination
                        bus = Bus.objects.filter(bus_id = int(arrroutes[2])).values('image','busConductor','conductorPhone','name')
                        anything["bus"]=bus
                        output.append(anything)
                if len(ticket2)>0:
                    print("in ticket2")
                    for items in ticket2:
                        anything1={}
                        strticket1 = str(items)
                        # anything1["strticket"]=strticket
                        arrticket1 = strticket1.split()
                        cost = int(arrticket1[2])
                        anything1["cost"]=cost
                        routesO = Routes.objects.filter(route_id = int(arrticket1[3]))
                        routesD = Routes.objects.filter(route_id = int(arrticket1[4]))
                        passticket = passengerTicket.objects.filter(pass_id = int(arrticket1[5])).values('name','birth_date','adhaarId')
                        trip1 = TripDate.objects.filter(trip_id = int(arrticket1[1])).values('tripDate')
                        anything1["routesD"]=routesD
                        anything1["passticket"]=passticket
                        anything1["routesO"]=routesO
                        anything1["trip1"]=trip1
                        strroutesO = str(routesO[0])
                        strroutesD = str(routesD[0])
                        # anything["strroutes"]=strroutes
                        arrroutesO = strroutesO.split()
                        arrroutesD = strroutesD.split()
                #         anything["arrroutes"]=arrroutes
                        busstandO = BusStand.objects.filter(id = int(arrroutesO[0]))
                        busstandD = BusStand.objects.filter(id = int(arrroutesD[1]))
                        # print(arrroutesO[0])
                        # print(int(arrroutesD[1]))
                        anything1["busstandO"]=busstandO
                        anything1["busstandD"]=busstandD
                        bus1 = Bus.objects.filter(bus_id = int(arrroutesO[2])).values('image','busConductor','conductorPhone','name')
                        anything1["bus1"]=bus1
                        output1.append(anything1)
                
                return render(request,'BusTracking/ticketchecker.html',{"passenger":passenger,"range":range(1,n_slides),"al":range(a),"output":output,"busstand":busstand,"output1":output1})
            else:
                error = True
                return render(request,'BusTracking/ticketchecker.html',{"error":error,"busstand":busstand})
    except Exception as e:
            print(e)
    return render(request,'BusTracking/ticketchecker.html',{"busstand":busstand})


def about(request):
    busstand = BusStand.objects.values('name')
    return render(request,'BusTracking/about.html',{"busstand":busstand})

def query(request):
    busstand = BusStand.objects.values('name')
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        query = Query(name=name,email=email,phone=phone,desc=desc)
        query.save()
        query_save = True 
        return render(request,'BusTracking/query.html',{"query_save":query_save,"busstand":busstand,"names":name})
    return render(request,'BusTracking/query.html',{"busstand":busstand})

def querylogin(request,myid):
    busstand = BusStand.objects.values('name')
    if request.method=="POST":
        passenger = Passenger.objects.filter(pass_id = myid)
        namestr = str(passenger[0])
        namearr = namestr.split()
        name = namearr[1]
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        query = Query(name=name,email=email,phone=phone,desc=desc)
        # where first name is which is in models and second one is in our if statements
        query.save()
        query_save = True 
        return render(request,'BusTracking/query.html',{"query_save":query_save,"busstand":busstand})
    return render(request,'BusTracking/query.html',{"busstand":busstand})
    



def searchbus(request):
    busstand = BusStand.objects.values('name')
    number = len(busstand)
    if request.method=="POST":
        destination = request.POST.get('cityT','')
        origin = request.POST.get('cityF','')   
        try: 
            busstandOrigin = BusStand.objects.filter(name = origin)
            busstandDestination = BusStand.objects.filter(name = destination)
            if(len(busstandOrigin)>0 and len(busstandDestination)>0):
                strdestination = (str)(busstandDestination[0])
                arrdestination = strdestination.split()
                busstandOrigin = BusStand.objects.filter(name = origin)
                strorigin = (str)(busstandOrigin[0])
                arrorigin = strorigin.split()
                try:
                    route = Routes.objects.filter(destination = arrdestination[1],origin=arrorigin[1])
                    if(len(route)>0):
                        allbusid=[]
                        cost=[]
                        allarrival=[]
                        alldeparture=[]
                        for item in route:
                            departure = ((str(item)).split())[6]
                            arrival = ((str(item)).split())[5]
                            allarrival.append([arrival])
                            alldeparture.append([departure])
                            strid = str(item)
                            arrid = strid.split()
                            allbusid.append([arrid[2]])
                            cost.append([arrid[4]])
                        allbusobj = []
                        i=0
                        for item in allbusid:
                            intid = int(item[0])
                            cost1 = int(cost[i][0])
                            arrival1 = (allarrival[i][0])
                            departure1 = (alldeparture[i][0])
                            bus = Bus.objects.filter(bus_id=intid).values('bus_id','name','Type','noOfSeats','busConductor','conductorPhone','image')
                            i+=1
                            allbusobj.append([bus,cost1,arrival1,departure1])
                        strroute = (str)(route[0])
                        arrroute = strroute.split()
                        route_id = arrroute[3]
                        thank = True
                        n = len(allbusobj)
                        n_slides = n//2 + ceil((n/2)-(n//2))
                        r = 1
                        return render(request,'BusTracking/searchbus.html',{"route":route,"allbusobj":allbusobj,"thank":thank,"busstand":busstand,"destination":destination,"origin":origin,"range":range(1,n_slides),"r":r})
                    else:
                        route1 = Routes.objects.filter(destination=arrdestination[1])
                        route2 = Routes.objects.filter(origin=arrorigin[1])
                        a = len(route1)
                        b = len(route2)
                        buss_ids = set()
                        for i in range(b):
                            for j in range(a):
                                if((str(route1[j]).split())[2]==(str(route2[i]).split())[2]):
                                    bus = Bus.objects.filter(bus_id =(str(route2[i]).split())[2] )
                                    buss_ids.add((str(route2[i]).split())[2])
                        arrbus_ids = list(buss_ids)
                        allbusobj = []
                        if(len(arrbus_ids)>0):
                            for item in arrbus_ids:
                                routeOrigin = Routes.objects.filter(bus_id=item,origin=arrorigin[1])
                                routeDestination = Routes.objects.filter(bus_id=item,destination=arrdestination[1])
                                allstationOriginTime=[]
                                allstationDestinationTime=[]
                                for i in range(len(routeOrigin)):
                                    stationTime = float((str(routeOrigin[i]).split())[5][0:2]+"."+(str(routeOrigin[i]).split())[5][3:5])
                                    allstationOriginTime.append(stationTime)
                                for i in range(len(routeDestination)):
                                    stationTime = float((str(routeDestination[i]).split())[5][0:2]+"."+(str(routeDestination[i]).split())[5][3:5])
                                    allstationDestinationTime.append(stationTime)
                                allstationDestinationTime.sort()
                                allstationOriginTime.sort()
                                b = len(allstationDestinationTime)
                                a = len(allstationOriginTime)
                                OriginTime=[]
                                DestinationTime=[]
                                if(a==1):
                                    for i in range(b):
                                        if allstationDestinationTime[i]>allstationOriginTime[0]:
                                            # print("In if of for of if firts")
                                            OriginTime.append(allstationOriginTime[0])
                                            DestinationTime.append(allstationDestinationTime[i])
                                            break
                                            pass
                                    pass
                                else:
                                    # print("In else first")
                                    if allstationDestinationTime[0]>allstationOriginTime[0]:
                                        # print("In if  of else firts")
                                        if allstationDestinationTime[0]>allstationOriginTime[1]:
                                            # print("In if  of if of else firts")
                                            OriginTime.append(allstationOriginTime[1])
                                            DestinationTime.append(allstationDestinationTime[0])
                                        else:
                                            # print("second else")
                                            OriginTime.append(allstationOriginTime[0])
                                            DestinationTime.append(allstationDestinationTime[0])
                                            pass
                                        pass
                                    else:
                                        # print("Third else")
                                        if b==2:
                                            # print("Third else in if ")
                                            OriginTime.append(allstationOriginTime[1])
                                            DestinationTime.append(allstationDestinationTime[1])

                                        pass
                                    pass
                                # now we get OriginTime and DestinationTime array and in both of them we have one element
                                routes = Routes.objects.filter(bus_id = item)
                                routes_id = []
                                for items in routes:
                                    stritmes = str(items)
                                    arritems = stritmes.split()
                                    Time = arritems[5]
                                    floatTime = float(Time[0:2]+"."+Time[3:5])
                                    # print(floatTime)
                                    if floatTime>=OriginTime[0] and floatTime<=DestinationTime[0]:
                                        # print("hello")
                                        route_id = int(arritems[3])
                                        routes_id.append(route_id)    
                                        pass
                                cost = 0
                                for itemss in routes_id:
                                    routes = Routes.objects.filter(route_id = itemss)
                                    routesOrigin = Routes.objects.filter(route_id = itemss,origin=arrorigin[1])
                                    if len(routesOrigin)>0:
                                        originstationtime = ((str(routesOrigin[0])).split())[5]
                                        routedOrigin = ((str(routesOrigin[0])).split())[3]
                                    routesDestination = Routes.objects.filter(route_id = itemss,destination=arrdestination[1])
                                    if len(routesDestination)>0:
                                        destinationstationtime = ((str(routesDestination[0])).split())[6]
                                        routedDestination = ((str(routesDestination[0])).split())[3]
                                        # print(routedDestination)
                                    arrroutes = str(routes[0]).split()
                                    cost = cost + int(arrroutes[4])
                                # print(routes_id)
                                # print(item)
                                # print(cost)
                                bus = Bus.objects.filter(bus_id=item).values('bus_id','name','Type','noOfSeats','busConductor','conductorPhone','image')
                                routesid = routes_id
                                allbusobj.append([bus,cost,originstationtime,destinationstationtime,routesid,routedOrigin,routedDestination,])

                            thank = True
                            r = 2
                            return render(request,'BusTracking/searchbus.html',{"busstand":busstand,"number":number,"thank":thank,"allbusobj":allbusobj,"destination":destination,"origin":origin,"r":r})
                        else:
                            error1 = True
                            return render(request,'BusTracking/searchbus.html',{"busstand":busstand,"number":number,"error1":error1})
                except Exception as e:
                    print(e)
            else:
                error2 = True
                return render(request,'BusTracking/searchbus.html',{"busstand":busstand,"number":number,"error2":error2})
        except Exception as e:
            print(e)
    return render(request,'BusTracking/searchbus.html',{"busstand":busstand,"number":number})



def pass_info(request,myid,pass_id,number):
    bus = Bus.objects.all()
    n = len(bus)
    n_slides = n//2 + ceil((n/2)-(n//2))
    busstand = BusStand.objects.values('name')
    if request.method=="POST":
        Pass_id = Passenger.objects.get(pass_id=pass_id)
        for x in range(1,number+1):
            
            print('date'+str(x))
            tripDate = request.POST.get(('date'+str(x)),'')
            name = request.POST.get(('name'+str(x)),'')
            # print(name)
            adhaarid = request.POST.get(('id'+str(x)),'')
            # adhaarid = int(adhaarid)
            bdate = request.POST.get(('bdate'+str(x)),'')
            passticket = passengerTicket(name=name,adhaarId=adhaarid,birth_date=bdate)
            passticket.save()
            strpassticket = str(passticket)
            # print(strpassticket)
            arrpassticket = strpassticket.split()
            passticketid = int(arrpassticket[0])
            tripdate = TripDate(tripDate=tripDate)
            tripdate.save()
            # print(tripdate)
            Passticket = passengerTicket.objects.get(pass_id = passticketid)
            arrtripdate=(str(tripdate)).split()
            trip_id = int(arrtripdate[0])
            # print(trip_id)
            route_id = myid
            Route_id = Routes.objects.get(route_id=route_id)
            Trip = TripDate.objects.get(trip_id=trip_id)
            ticket = Tickets(passenger=Pass_id,routes=Route_id,trip=Trip,ticketpassenger=Passticket)
            ticket.save()
            strTicket_id = (str)(ticket)
            arrTicket_id = strTicket_id.split()
            ticket_id = (int)(arrTicket_id[1])
            pass_id = (int)(pass_id)
        passenger_save = True 
        return render(request,'BusTracking/index.html',{"passenger_save":passenger_save,"busstand":busstand,"bus":bus,"range":range(1,n_slides),})
    return render(request,'BusTracking/index.html',{"busstand":busstand,"bus":bus,"range":range(1,n_slides),})


def bookpass_info(request,pass_id,number):
    busstand = BusStand.objects.values('name')
    bus = Bus.objects.all()
    n = len(bus)
    n_slides = n//2 + ceil((n/2)-(n//2))
    if request.method=="POST":
        Pass_id = Passenger.objects.get(pass_id=pass_id)
        cost = request.POST.get('cost','')
        roid = request.POST.get('roid','')
        rdid = request.POST.get('rdid','')
        roid = Routes.objects.get(route_id=roid)
        rdid = Routes.objects.get(route_id=rdid)
        for x in range(1,number+1):
            tripDate = request.POST.get(('date'+str(x)),'')
            name = request.POST.get(('name'+str(x)),'')
            # print(name)
            adhaarid = request.POST.get(('id'+str(x)),'')
            # adhaarid = int(adhaarid)
            bdate = request.POST.get(('bdate'+str(x)),'')
            passticket = passengerTicket(name=name,adhaarId=adhaarid,birth_date=bdate)
            passticket.save()
            strpassticket = str(passticket)
            # print(strpassticket)
            arrpassticket = strpassticket.split()
            passticketid = int(arrpassticket[0])
            tripdate = TripDate(tripDate=tripDate)
            tripdate.save()
            Passticket = passengerTicket.objects.get(pass_id = passticketid)
            routesid = request.POST.get('routeid','')
            arrtripdate=(str(tripdate)).split()
            trip_id = int(arrtripdate[0])
            Trip = TripDate.objects.get(trip_id=trip_id)
            ticket = BookMultipleRoutesTickets(passenger=Pass_id,routes=routesid,trip=Trip,routeOrigin=roid,cost=cost,routeDestination=rdid,ticketpassenger=Passticket)
            ticket.save()
            strTicket_id = (str)(ticket)
            arrTicket_id = strTicket_id.split()
            ticket_id = (int)(arrTicket_id[0])
            pass_id = (int)(pass_id)
        passenger_save = True 
        return render(request,'BusTracking/index.html',{"passenger_save":passenger_save,"busstand":busstand,"bus":bus,"range":range(1,n_slides),})
    return render(request,'BusTracking/index.html',{"busstand":busstand,"bus":bus,"range":range(1,n_slides),})

def busview(request,id):
    bus = Bus.objects.filter(bus_id = id).values('bus_id','name','Type','noOfSeats','busConductor','conductorPhone','image')
    busstand = BusStand.objects.filter(bus = id).values('name')
    return render(request,'BusTracking/busview.html',{"bus":bus,"busstand":busstand})

def handlesignup(request):
    busstand = BusStand.objects.values('name')
    bus = Bus.objects.all()
    n = len(bus)
    n_slides = n//2 + ceil((n/2)-(n//2))
    if request.method=="POST":
        # get the post parameters
        username = request.POST.get('username','')
        firstName = request.POST.get('fname','')
        lastName = request.POST.get('lname','')
        email = request.POST.get('email','')
        addhaar_id = request.POST.get('id','')
        B_date = request.POST.get('bdate','')
        password1 = request.POST.get('password','')
        password2 = request.POST.get('password1','')
        # check errorneous input
        if len(username) > 10:
            error1 = True
            return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"error":error1})
        if not username.isalnum():
            error2 = True
            return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"error":error2})
        if password1!=password2:
            error3 = True
            return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"error":error3})
        # create the user
        passenger = Passenger(name=firstName+" " + lastName,adhaarId = addhaar_id,birth_date = B_date)
        passenger.save()
        strpassenger = str(passenger)
        arrpassenger  = strpassenger.split()
        passenger_id = int(arrpassenger[0])
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myextenduser = extenduser(adhaarId = addhaar_id , birth_date = B_date , pass_id =passenger_id , user  = myuser )
        myextenduser.save()
        myuser.save()
        signups = True
        return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"signups":signups})

    else:
        return HttpResponse('404 error found')

def handlelogin(request):
    busstand = BusStand.objects.values('name')
    bus = Bus.objects.all()
    n = len(bus)
    n_slides = n//2 + ceil((n/2)-(n//2))
    if request.method=="POST":
        # get the post parameters
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            logins = True
            datas = extenduser.objects.filter(user = request.user)
            # print(datas)
            strdatas = str(datas[0])
            arrdatas = strdatas.split()
            pass_id = int(arrdatas[0])
            birth_date = arrdatas[1]
            adhaarId = arrdatas[2]
            return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"logins":logins,"email":user.email,"firstName":user.first_name,"lastName":user.last_name,"pass_id":pass_id,"birth_date":birth_date,"adhaarId":adhaarId})
        else:
            error4=True
            return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"error4":error4})
    else:
        return HttpResponse('404 error found')

def handlelogout(request):
    busstand = BusStand.objects.values('name')
    bus = Bus.objects.all()
    n = len(bus)
    n_slides = n//2 + ceil((n/2)-(n//2))
    logout(request)
    logouts = True
    return render(request,'BusTracking/index.html',{"bus":bus,"range":range(1,n_slides),"busstand":busstand,"logouts":logouts})


def directbookticket(request,myid):
    busstand = BusStand.objects.values('name')
    number = len(busstand)
    if request.method=="POST":
        destination = request.POST.get('to','')
        number = request.POST.get('number','')
        number = int(number)
        destination=destination[4:]
        print(destination)
        origin = request.POST.get('from','')   
        origin=origin[6:]
        print(origin)
        Busid = request.POST.get('id','') 
        
        Busid=Busid[4:]
        print(Busid)
        r = request.POST.get('r','')   
        print(r)
        r=int(r)
        busstandOrigin = BusStand.objects.filter(name = origin)
        busstandDestination = BusStand.objects.filter(name = destination)
        strdestination = (str)(busstandDestination[0])
        arrdestination = strdestination.split()
        strorigin = (str)(busstandOrigin[0])
        arrorigin = strorigin.split()
        if r==1:
            routes = Routes.objects.filter(destination = arrdestination[1],origin=arrorigin[1],bus=Busid)
            strroute = (str)(routes[0])
            arrroute = strroute.split()
            route_id = arrroute[3]
            R = False
            return render(request,'BusTracking/pass_info.html',{"route_id":route_id,"pass_id":myid,"busstand":busstand,"R":R,"range":range(number),"number":number})
        else:
            arrayrouteid = request.POST.get('rid')
            roid = request.POST.get('roid','') 
            rdid = request.POST.get('rdid','') 
            cost = request.POST.get('cost','')[6:]
            print(arrayrouteid)
            R = True
            return render(request,'BusTracking/pass_info.html',{"arrayrouteid":arrayrouteid,"pass_id":myid,"busstand":busstand,"R":R,"cost":cost,"rdid":rdid,"roid":roid,"range":range(number),"number":number})
    else:
        return HttpResponse("if else")
   