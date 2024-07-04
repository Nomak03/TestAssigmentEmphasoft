from django.db import models
from django.contrib.auth.models import User


class HotelUser(User):
    email = models.EmailField(blank=False, unique=True, null=False)



