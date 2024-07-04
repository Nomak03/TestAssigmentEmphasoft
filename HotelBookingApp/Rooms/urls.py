from django.urls import path
from .views import GetRoomsView, GetUserBookedRoomsView, BookedRoom, CanceledBooking

urlpatterns = [
    path("index/", GetRoomsView.as_view()),
    path("booked/", GetUserBookedRoomsView.as_view()),
    path("book/", BookedRoom.as_view()),
    path("cancel/", CanceledBooking.as_view())
]
