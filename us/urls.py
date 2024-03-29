from django.urls import path
from . import views

app_name = 'us'
urlpatterns = [
    path("career/", views.Career.as_view(), name='career'),
    path("custumers/", views.Customers.as_view(), name='customers'),
    path("contactus/", views.Contactus.as_view(), name='contactus'),
    path("aboutus/", views.AboutUs.as_view(), name='aboutus'),
]