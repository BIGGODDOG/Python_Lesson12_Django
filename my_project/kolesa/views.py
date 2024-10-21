from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from kolesa.models import Car, Customer
from kolesa.forms import CarForm, CustomerForm, UserRegistrationForm
from django.db.models import Count, Avg
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class CarListView(ListView):
    model = Car
    context_object_name = "cars"

    def get_queryset(self):
        return self.model.objects.filter(in_stock=True)

class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg: str = "car_id"
    
class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("car_list")
    template_name: str = "kolesa/car_form.html"

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("car_list")
    template_name: str = "kolesa/car_form.html"
    pk_url_kwarg: str = "car_id"

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("car_list")
    template_name: str = "kolesa/car_form.html"
    pk_url_kwarg: str = "car_id"



class CustomerListView(ListView):
    model = Customer
    context_object_name = "customers"

class CustomerDetailView(DetailView):
    model = Customer
    pk_url_kwarg: str = "customer_id"
    
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customer_list")
    template_name: str = "kolesa/customer_form.html"

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customer_list")
    template_name: str = "kolesa/customer_form.html"
    pk_url_kwarg: str = "customer_id"

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer_list")
    template_name: str = "kolesa/customer_form.html"
    pk_url_kwarg: str = "customer_id"



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

