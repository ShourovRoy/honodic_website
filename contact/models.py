from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=False, blank=False, null=False, max_length=200)
    subject = models.CharField(max_length=300, blank=False, null=False)
    message = models.TextField(max_length=2000, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.subject



class ContactDetail(models.Model):
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    contact_email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.TextField(max_length=500, blank=False, null=False)
    facebook_link = models.URLField(max_length=800, blank=True, null=True)
    twitter_link = models.URLField(max_length=800, blank=True, null=True)
    instagram_link = models.URLField(max_length=800, blank=True, null=True)
    linkdin_link = models.URLField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.phone_number