from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .services import contact
from .serializers import ContactSerializer

# Create your views here.
def get_contacts(request):
    return contact.get_contacts(request)

def get_contact(request, pk):
    return contact.get_contact(request, pk)

class ContactViewSet(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated]


