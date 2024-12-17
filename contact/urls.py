from django.urls import path

from .views import send_message

app_name = 'contact';
urlpatterns = [
    path("contact/", send_message, name="contact_view"),
]