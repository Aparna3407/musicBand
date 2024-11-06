from django.contrib import admin
from .models import Subscriber
from .models import Instrumentalists, Vocalists, Management, GalleryImage, Contactdetails, Concerts

# Register your models here.
admin.site.register(Instrumentalists)
admin.site.register(Vocalists)
admin.site.register(Management)
admin.site.register(GalleryImage)
admin.site.register(Contactdetails)
admin.site.register(Concerts)
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
