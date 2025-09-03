from django import forms
from .models import Reservations


class TableReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ["customer_name", "phone", "email", "no_of_guests"]

        labels = {
            "cusomer_name": "Customer Name",
            "phone": "Mobile Number",
            "email": "Email Address",
            "no_of_guests": "Number of Guests",
        }

        help_texts = {
            "phone": "Enter a valid 10-digit mobile number.",
            "no_of_guests": "Enter the number of people in your group.",
        }

    def clean(self):
        cleaned_data = super().clean()

        phone = cleaned_data.get("phone")
        guests = cleaned_data.get("no_of_guests")

        # Phone validation
        if phone:
            phone_str = str(phone)
            if not phone_str.isdigit():
                self.add_error("phone", "Phone number must contain only digits.")
            elif len(phone_str) != 10:
                self.add_error("phone", "Phone number must be exactly 10 digits.")

        # Guest validation
        if guests is not None:
            if guests < 1:
                self.add_error("no_of_guests", "Minimum number of guests is 1.")
            elif guests > 20:
                self.add_error("no_of_guests", "We cannot take reservations for more than 20 guests.")

        return cleaned_data
