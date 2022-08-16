from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=12)

    def __str__(self):
        return self.name