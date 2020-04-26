from django.urls import path, include
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'rooms', views.CategoryViewSet)

urlpatterns = [
    #path('hotels/', views.HotelView.as_view())
    path('info/', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('info/roomcategories/', views.RoomCategoriesInHotelListView.as_view(), name='room-categories'),
    path('info/rooms/', views.RoomsInHotelListView.as_view(), name='rooms'),
    path('info/hotels/', views.HotelsListView.as_view(), name='hotels'),
    path('info/users/', views.UsersListView.as_view(), name='users'),
    path('info/bookings/', views.BookingsListView.as_view(), name='bookings'),
    path('info/roomcategories/<str:cat>/', views.CategoryListView.as_view(), name='chosen-category'),
]

