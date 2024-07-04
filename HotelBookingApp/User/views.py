from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from Rooms.serializers import UserSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None or password is None:
            return Response({'error': 'Введите логин или пароль'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'error': 'Неверные данные'},
                            status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        refresh.payload.update({
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):

        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'Необходим refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': 'Неверный refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Выход успешен'}, status=status.HTTP_200_OK)
