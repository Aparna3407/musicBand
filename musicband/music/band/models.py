from django.db import models
from PIL import Image

# Create your models here.
class Instrumentalists(models.Model):
    img=models.ImageField(upload_to='pictures')
    name=models.CharField(max_length=250)
    instrument=models.CharField(max_length=250)
    details=models.TextField()

    def __str__(self):
        return self.name

class Vocalists(models.Model):
    img=models.ImageField(upload_to='pictures')
    name=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    details=models.TextField()

    def __str__(self):
        return self.name

class Management(models.Model):
    img = models.ImageField(upload_to='pictures')
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    details = models.TextField()

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name

class Contactdetails(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone=models.IntegerField()
    msg=models.TextField()

    def __str__(self):
        return self.name

class Concerts(models.Model):
    concert_id=models.IntegerField()
    name=models.CharField(max_length=250)
    date=models.DateTimeField()
    place=models.CharField(max_length=250)
    total_tickets = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Ticket(models.Model):
    show = models.ForeignKey(Concerts, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Ticket for {self.show.name} by {self.buyer_name}'