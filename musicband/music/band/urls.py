from django.urls import path
from . import views
from .views import concerts, purchase_ticket


urlpatterns=[
    path('',views.index,name='index'),
    path('profiles/',views.profiles,name='profiles'),
    path('concerts/',views.concerts,name='concerts'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    # path('concerts/',views.concerts,name=concerts),
    path('purchase/<int:concert_id>/', purchase_ticket, name='purchase_ticket'),

]