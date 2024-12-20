from .models import ContactDetail


def contact_details_view(request):

    contact_details = ContactDetail.objects.get();

    context = {
        "contact_details": contact_details 
    }

    return context

