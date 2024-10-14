from django.shortcuts import get_object_or_404, redirect, render
from phonebook.forms import ConfirmDeleteForm, ContactForm
from phonebook.models import Contact

# Create your views here.

def contact_list(request):
    contacts = Contact.objects.all()

    context = {
        "contacts": contacts,
        }
    return render(request, "phonebook/contact_list.html", context)

def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, "phonebook/contact_detail.html", {"contact": contact})

def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else: 
        form = ContactForm()
    return render(request, "phonebook/contact_form.html", {"form": form})

def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "phonebook/contact_form.html", {"form": form})

def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, id = contact_id)

    if request.method == "POST":
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirm"]:
            contact.delete()
            return redirect("contact_list")
    else:
        form = ConfirmDeleteForm()
    return render(request, "phonebook/contact_form.html", {"form": form})