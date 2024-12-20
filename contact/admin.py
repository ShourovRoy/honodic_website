from django.contrib import admin
from .models import ContactMessage, ContactDetail

# Register your models here.
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ["phone_number", "contact_email"]



admin.site.register(ContactMessage)
admin.site.register(ContactDetail, ContactDetailsAdmin)