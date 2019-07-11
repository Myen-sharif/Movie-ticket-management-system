

from django.urls import path
from . import views

urlpatterns = [


    path('', views.homepage, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('contacts/',views.contacts, name='contacts'),
    path('movieselect/',views.selectMovie, name='selectmovie'),
    path('nowshowing/', views.nowshowing, name='nowshowing'),
    path('payment/', views.payment, name='payment'),
    path('seatslayout/', views.seatslayout, name='seatslayout'),
    path('printticket/', views.printticket, name='printticket'),
    path('ticketprice/', views.ticketprice, name='ticketprice'),


]
