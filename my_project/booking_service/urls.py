from django.urls import path
from booking_service.views import RoomListView, room_list, room_detail, room_create, room_update, room_delete, check_availability, register, RoomDetailView, RoomCreateView, RoomUpdateView, RoomDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("rooms/", RoomListView.as_view(), name="room_list"),
    path("rooms/<int:room_id>", RoomDetailView.as_view(), name="room_detail"),
    path("room_create/", RoomCreateView.as_view(), name="room_create"),
    path("room_update/<int:room_id>", RoomUpdateView.as_view(), name="room_update"),
    path("room_delete/<int:room_id>", RoomDeleteView.as_view(), name="room_delete"),
    path("check_availability/", check_availability, name="check_availability"),
    path("register/", register, name="registration"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]