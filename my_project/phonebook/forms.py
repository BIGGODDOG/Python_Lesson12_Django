from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        return name
    
class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Вы уверены что хотите удалить контакт?")
