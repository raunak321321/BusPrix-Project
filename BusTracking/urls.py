# I made this file
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="BusHome"),
    path('ticketchecker/<int:myid>/', views.ticketchecker,name="BusTicketHome"),
    path('about/', views.about,name="BusAbout"),
    path('query/', views.query,name="BusQuery"),
    path('query/<int:myid>/', views.querylogin,name="BusQuery2"),
    path('directbooktickets/<int:myid>/', views.directbookticket,name="BusBookTicketHome3"),
    path('bookticket/<int:myid>/<int:pass_id>/<int:number>/', views.pass_info,name="pass_info"),
    path('bookmultipleticket/<int:pass_id>/<int:number>/', views.bookpass_info,name="pass_info2"),
    path('busview/<int:id>/', views.busview,name="busview"),
    path('searchbus/', views.searchbus,name="searchbus"),
    path('signup/', views.handlesignup,name="signup"),
    path('login/', views.handlelogin,name="login"),
    path('logout/', views.handlelogout,name="logout"),
]