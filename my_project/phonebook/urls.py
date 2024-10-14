from django.urls import path, re_path
from phonebook.views import contact_delete, contact_list, contact_detail, contact_create, contact_update

urlpatterns = [
    path("contacts/", contact_list, name="contact_list"),
    path("contacts/<int:contact_id>", contact_detail, name="contact_detail"),
    path("contact_create/", contact_create, name="contact_create"),
    path("contact_update/<int:contact_id>", contact_update, name="contact_update"),
    path("contact_delete/<int:contact_id>", contact_delete, name="contact_delete"),
]