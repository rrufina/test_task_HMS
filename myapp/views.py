from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

'''
List of enpoints:
- User registration
- User logout
- User change password
- List hotels (only for admin users)
- List RoomCategory (only for hotel related users)
- List Rooms (only for hotel related users)
- List Rooms of some RoomCategory (only for hotel related users)
- List Bookings (only for hotel related users)
- List Bookings of some Room (only for hotel related users)
- Create booking List Bookings (only for hotel related users), care about overlappings
- Get for Room, Booking, RoomCategory, Hotel (only for hotel related users)
- User (only for admin users)
'''


def index(request):
    return render(request, 'index.html')

'''
class HotelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hotels to be viewed or edited.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAdminUser]
'''


class RoomCategoriesInHotelListView(LoginRequiredMixin, generic.ListView):
    model = RoomCategory
    template_name = 'info/room_categories_list.html'

    def get_queryset(self):
        hotel_user = HotelUser.objects.filter(user=self.request.user).first()
        return RoomCategory.objects.filter(hotel=hotel_user.hotel).order_by('min_price')


class RoomsInHotelListView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'info/room_list.html'

    def get_queryset(self):
        hotel_user = HotelUser.objects.filter(user=self.request.user).first()
        r_c = list(RoomCategory.objects.filter(hotel=hotel_user.hotel))
        return Room.objects.filter(room_category__in=r_c).order_by('name')


class HotelsListView(LoginRequiredMixin, generic.ListView):
    model = Hotel
    template_name = 'info/hotel_list.html'
    def get_queryset(self):
        return Hotel.objects.all().order_by('name')


class UsersListView(LoginRequiredMixin, generic.ListView):
    model = HotelUser
    template_name = 'info/user_list.html'
    def get_queryset(self):
        return HotelUser.objects.all().order_by('hotel')


class BookingsListView(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = 'info/bookings_list.html'

    def get_queryset(self):
        hotel_user = HotelUser.objects.filter(user=self.request.user).first()
        categories = list(RoomCategory.objects.filter(hotel=hotel_user.hotel))
        rooms = list(Room.objects.filter(room_category__in=categories))
        return Booking.objects.filter(room__in=rooms).order_by('room')


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'info/room_list.html'

    def get_queryset(self, cat=None):
        print(cat)
        hotel_user = HotelUser.objects.filter(user=self.request.user).first()
        category = RoomCategory.objects.filter(hotel=hotel_user.hotel, name=cat).first()
        return Room.objects.filter(room_category=category).order_by('name')

