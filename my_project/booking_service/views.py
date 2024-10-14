from django.shortcuts import redirect, render
from booking_service.models import Room
from django.shortcuts import get_object_or_404
from booking_service.forms import AvailabilityForm, RoomForm, ConfirmDeleteForm
from django.db.models import Q, Count, Avg
from booking_service.utils import get_available_rooms

# Create your views here.

def room_list(request):
    rooms = Room.objects.annotate(booking_count=Count("booking"))
    average_price = Room.objects.aaggregate(Avg("price"))
    # rooms = Room.objects.filter(price = 70)
    # rooms = Room.objects.filter(price__lt=150)
    # rooms = Room.objects.filter(price__lte=150)
    # rooms = Room.objects.filter(price__gt=150)
    # rooms = Room.objects.filter(price__gte=150)
    # rooms = Room.objects.filter(price__range=(100, 149))
    # rooms = Room.objects.filter(name__icontains="room")
    # rooms = Room.objects.filter(name__startswith="A")
    # rooms = Room.objects.filter(Q(name="my_room") | Q(name="office"))
    # rooms = Room.objects.filter(Q(name="my_room") & Q(price__gt=100))
    # rooms = Room.objects.filter(Q(name="my_room") & ~Q(price__gt=100))
    context = {
        "rooms": rooms,
        "avg_price": average_price
        }
    return render(request, "booking_service/room_list.html", context)

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, "booking_service/room_detail.html", {"room": room})

def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else: 
        form = RoomForm()
    return render(request, "booking_service/room_form.html", {"form": form})

def room_update(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(instance=room)
    return render(request, "booking_service/room_form.html", {"form": form})

def room_delete(request, room_id):
    room = get_object_or_404(Room, id = room_id)

    if request.method == "POST":
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirm"]:
            room.delete()
            return redirect("room_list")
    else:
        form = ConfirmDeleteForm()
    return render(request, "booking_service/room_form.html", {"form": form})

def check_availability(request):
    available_rooms = None
    form = AvailabilityForm(request.GET)

    if form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        available_rooms = get_available_rooms(start_date, end_date)

    return render(request, "booking_service/check_availability.html", {"form": form, "available_rooms": available_rooms})