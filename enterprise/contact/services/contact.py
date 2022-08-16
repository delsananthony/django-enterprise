from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from ..models import Contact

def get_contacts(request):

    contacts = Contact.objects.all()
    data = {
        "results": list(contacts.values("name"))
    }

    return JsonResponse(data)

def get_contact(request, pk):

    contact = get_object_or_404(Contact, pk=pk)
    data = {
        "results": {
            "id": contact.id,
            "name": contact.name
        }
    }

    return JsonResponse(data)
