from django.urls import path

from .views import about_us_view

app_name = 'about';
urlpatterns = [
    path("about/", about_us_view, name="about_us_view"),
]