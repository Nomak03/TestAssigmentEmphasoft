from django.contrib import admin
from .models import Room, BookedRoom


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'price', 'places_amount', 'is_booked')
    list_filter = ('is_booked', 'price', 'places_amount',)


@admin.register(BookedRoom)
class BookedRoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'checkin_date', 'checkout_date',)
    list_filter = ('checkin_date', 'checkout_date',)
