from django.urls import path
from kolesa.views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("cars/", CarListView.as_view(), name="car_list"),
    path("cars/<int:car_id>", CarDetailView.as_view(), name="car_detail"),
    path("car_create/", CarCreateView.as_view(), name="car_create"),
    path("car_update/<int:car_id>", CarUpdateView.as_view(), name="car_update"),
    path("car_delete/<int:car_id>", CarDeleteView.as_view(), name="car_delete"),

    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/<int:customer_id>", CustomerDetailView.as_view(), name="customer_detail"),
    path("customer_create/", CustomerCreateView.as_view(), name="customer_create"),
    path("customer_update/<int:customer_id>", CustomerUpdateView.as_view(), name="customer_update"),
    path("customer_delete/<int:customer_id>", CustomerDeleteView.as_view(), name="customer_delete"),

    path("register/", register, name="registration"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]