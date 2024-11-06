from django.utils import timezone

from .models import Instrumentalists, Vocalists, Management, GalleryImage, Contactdetails,Concerts
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import SubscriptionForm
from django.forms import ModelForm
from .forms import TicketPurchaseForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def profiles(request):
    obj = Instrumentalists.objects.all()
    res = Vocalists.objects.all()
    out = Management.objects.all()
    return render(request, 'profiles.html', {'display': obj, 'result': res, 'outcome': out})

def concerts(request):
    shows=Concerts.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'concerts.html', {'shows': shows})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'pictures': images})

class ContactForm(ModelForm):
    class Meta:
        model = Contactdetails
        fields = ['name', 'email', 'phone', 'msg']

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Use the form instance to handle data and validation

        if form.is_valid():
            # Save the contact details to the database
            contact_instance = form.save()

            try:
                # Construct the message
                full_message = (
                    f"Name: {contact_instance.name}\n"
                    f"Email: {contact_instance.email}\n"
                    f"Phone: {contact_instance.phone}\n\n"
                    f"Message:\n{contact_instance.msg}"
                )

                # Send an email
                send_mail(
                    subject=f"Message from {contact_instance.name} via Contact Form",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,  # Ensure this is defined in settings.py
                    recipient_list=[settings.DEFAULT_TO_EMAIL],  # Ensure this is defined in settings.py
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"There was an error sending your message. {str(e)}")
        else:
            # If the form is invalid, display an error message
            messages.error(request, "Please correct the errors below.")

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully subscribed!")
        return redirect('subscribe')
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})

def purchase_ticket(request, concert_id):
    show = get_object_or_404(Concerts, id=concert_id)

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        form.instance.show = show  # Set the show instance

        if form.is_valid():
            ticket = form.save()
            show.total_tickets -= ticket.quantity
            show.save()
            return redirect('concerts')  # Redirect to show list after purchase

    else:
        form = TicketPurchaseForm()

    return render(request, 'purchaseticket.html', {'form': form, 'show': show})
