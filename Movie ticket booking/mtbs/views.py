from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration1.html')

def contacts(request):
    return render(request, 'contacts.html')

def selectMovie(request):
    return render(request, 'MovieSelect.html')

def nowshowing(request):
    return render(request, 'nowshowing.html')

def payment(request):
    return render(request, 'Payment.html')

def seatslayout(request):
    return render(request,'SeatsLayout.html')

def printticket(request):
    return render(request,'printTicket.html')

def ticketprice(request):
    return render(request,'ticketPrice.html')


