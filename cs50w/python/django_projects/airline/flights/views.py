from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger



def checkFlight(request, flight_id):
    """
    Check if a flight exists in the database.
    """
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {
            "message": f"Flight {flight_id} not found."
        })
    return flight
    
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = checkFlight(request=request, flight_id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    flight = None
    
    if request.method == "POST":
        flight = checkFlight(flight_id=flight_id, request=request)
        passenger_id = int(request.POST.get("passenger"))
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
    
    return render(request, "flights/book.html", {
        "flight": flight
    })