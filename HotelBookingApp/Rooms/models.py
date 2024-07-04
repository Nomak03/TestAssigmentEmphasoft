from django.db import models
from User.models import HotelUser


class Room(models.Model):
    id = models.UUIDField(auto_created=True)
    room_number = models.IntegerField(unique=True)
    price = models.FloatField()
    places_amount = models.SmallIntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Комната №{self.room_number}"


class BookedRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(HotelUser, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()

    def __str__(self):
        return f"Комната забронирована с {self.checkin_date} до {self.checkout_date}"

