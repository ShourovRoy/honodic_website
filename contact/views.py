from django.shortcuts import render
from .models import ContactMessage
from django.contrib import messages


# Create your views here.
def send_message(request):

    if request.method == "POST":
        try:
            form = request.POST
            first_name = form.get("first_name");
            last_name = form.get("last_name");
            email = form.get("email");
            subject = form.get("subject");
            message = form.get("message");
        
            ContactMessage(
                first_name=first_name,
                last_name=last_name,
                email=email,
                subject=subject,
                message=message,
            ).save()

            messages.success(request, "Thanks for contacting us. We will get back to you soon.")
        except:
            messages.error(request, "Faild to send the message.")


    context = {
        "message": "Hello contact"
    }
    return render(request, "contact/contact.html", context)