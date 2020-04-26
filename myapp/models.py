from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_check_in = models.DateTimeField('date check in')
    date_check_out = models.DateTimeField('date check out')


class HotelUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
