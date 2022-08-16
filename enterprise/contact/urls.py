from django.urls import path
from .views import get_contacts, get_contact

urlpatterns = [
    path('', get_contacts, name='contact-list'),
    path('<int:pk>/', get_contact, name='contact-detail'),
]