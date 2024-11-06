from django import forms
from .models import Subscriber,Concerts
from .models import Ticket


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})
        }



class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['buyer_name', 'buyer_email', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        show = self.instance.show
        if quantity > show.total_tickets:
            raise forms.ValidationError("Not enough tickets available.")
        return quantity
