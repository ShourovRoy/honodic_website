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

