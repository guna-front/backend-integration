
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)       # store name
    email = models.EmailField()                    # store email
    message = models.TextField()                   # store message
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)       # store name
    email = models.EmailField()                    # store email
    message = models.TextField()                   # store message
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

