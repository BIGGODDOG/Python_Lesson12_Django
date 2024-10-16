from django.urls import path, re_path
from booking_service.views import room_list, room_detail, room_create, room_update, room_delete, check_availability

urlpatterns = [
    path("rooms/", room_list, name="room_list"),
    path("rooms/<int:room_id>", room_detail, name="room_detail"),
    path("room_create/", room_create, name="room_create"),
    path("room_update/<int:room_id>", room_update, name="room_update"),
    path("room_delete/<int:room_id>", room_delete, name="room_delete"),
    path("check_availability/", check_availability, name="check_availability"),
]