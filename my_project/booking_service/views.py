from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from booking_service.models import Room
from django.shortcuts import get_object_or_404
from booking_service.forms import AvailabilityForm, RoomForm, ConfirmDeleteForm, UserRegistrationForm
from django.db.models import Count, Avg
from booking_service.utils import get_available_rooms
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
# from booking_service.signal import my_signal
# Create your views here.

# def mock_user_required(request, view):
#     if request.user: 
#         return view(request)

class RoomListView(LoginRequiredMixin, ListView):
    model = Room
    context_object_name = "rooms"
    # extra_content = {}

    # permission_required = "booking_service.view_room"

    # def test_func(self) -> bool:
    #     return self.request.user.is_superuser

    def get_queryset(self):
        # my_signal.send("My sender")
        return self.model.objects.annotate(booking_count=Count("booking"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avg_price"] = self.model.objects.aggregate(Avg("price"))["price__avg"]
        return context

class RoomDetailView(DetailView):
    model = Room
    pk_url_kwarg: str = "room_id"

    # def get_object(self, queryset):
    #     return self.get_queryset().get(pk=self.object_id)
    
class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy("room_list")
    template_name: str = "booking_service/room_form.html"

class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy("room_list")
    template_name: str = "booking_service/room_form.html"
    pk_url_kwarg: str = "room_id"

class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy("room_list")
    template_name: str = "booking_service/room_form.html"
    pk_url_kwarg: str = "room_id"

@login_required
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

    response = render(request, "booking_service/check_availability.html", {"form": form, "available_rooms": available_rooms})

    # Работа с Cookies
    # response.set_cookie("my_cookie", "19")
    # response.set_signed_cookie("my_cookie", "19", salt="123sqadqwe")
    # cookies = request.COOKIES
    # my_cookie = request.get_signed_cookie("cookie_key")

    return response

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("room_list")
    else:
        form = UserRegistrationForm()
    return render(request, "booking_service/register.html", {"form": form})



def get_json_rooms(request):
    objects = Room.objects.all()

    data = [{"id": obj.id, "name": obj.name} for obj in objects]

    return JsonResponse(data, safe=False)