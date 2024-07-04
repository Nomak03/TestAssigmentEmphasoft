from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import RoomSerializer, BookedRoomSerializer
from .models import Room, BookedRoom


class GetRoomsView(APIView):
    def get(self, request: Request):
        queryset = Room.objects.exclude(is_booked=True)
        serializer = RoomSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class GetUserBookedRoomsView(APIView):

    permission_classes = [IsAuthenticated]

    def get_user_booked_room(self, request: Request):
        queryset = BookedRoom.objects.filter(user=request.data.get('email'))
        serializer = BookedRoomSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class BookedRoom(APIView):

    permission_classes = [IsAuthenticated]

    def book_room(self, request: Request):
        serializer = BookedRoomSerializer(data=request.data)
        if serializer.room not in BookedRoom.objects.all:
            booked_room = BookedRoom()
            room = Room.objects.get(id=serializer.room.id)
            booked_room.room = serializer.room
            booked_room.user = serializer.user
            booked_room.checkin_date = serializer.checkin_date
            booked_room.checkout_date = serializer.checkout_date
            room.is_booked = True
            room.save()
            booked_room.save()
        return Response({'success': 'Комната забронирована'}, status=status.HTTP_201_CREATED)


class CanceledBooking(APIView):

    permission_classes = [IsAuthenticated]

    def delete_booked_room(self, request: Request):
        serializer = BookedRoomSerializer(data=request.data)
        if serializer.room in BookedRoom.objects.all:
            booked_room = BookedRoom.objects.get(room=serializer.room)
            room = Room.objects.get(id=serializer.room.id)
            room.is_booked = False
            room.save()
            booked_room.delete()

        return Response({'success': 'Бронь отменена'}, status=status.HTTP_200_OK)


