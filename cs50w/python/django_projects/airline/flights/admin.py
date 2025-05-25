from django.contrib import admin

from .models import Flight, Airport, Passenger


# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    search_fields = ("origin__city", "destination__city")
    list_filter = ("origin", "destination")
    ordering = ("origin", "destination")

class AirportAdmin(admin.ModelAdmin):
    list_display = ("code", "city")
    search_fields = ("code", "city")
    list_filter = ("code", "city")
    ordering = ("code", "city")

class PassengerAdmin(admin.ModelAdmin):
    list_display = ("first", "last")
    search_fields = ("first", "last")
    list_filter = ("first", "last")
    filter_horizontal = ("flights",)
    ordering = ("first", "last")


admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Passenger, PassengerAdmin)