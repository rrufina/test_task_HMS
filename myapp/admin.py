from django.contrib import admin
from .models import *


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelUser)
class HotelUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_category', 'name')


@admin.register(RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'name', 'min_price')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'date_check_in', 'date_check_in')
