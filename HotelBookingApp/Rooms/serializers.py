from rest_framework import fields, serializers
from .models import Room, BookedRoom
from User.models import HotelUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelUser
        fields = ('first_name', 'last_name', 'email',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room_number', 'price', 'places_amount', 'is_booked')


class BookedRoomSerializer(serializers.ModelSerializer):
    user = UserSerializer
    room = RoomSerializer

    class Meta:
        model = BookedRoom
        fields = ('room', 'user', 'checkin_date', 'checkout_date',)
