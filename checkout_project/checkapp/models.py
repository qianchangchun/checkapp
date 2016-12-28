from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Computer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_available = models.BooleanField(default=True)
    added_by = models.CharField(max_length=200, blank=True, null=True)
    added_date = models.DateTimeField(blank=True, null=True)
    checkin_date = models.DateTimeField(blank=True, null=True)
    checkout_date = models.DateTimeField(blank=True, null=True)
    checked_in_by = models.CharField(max_length=200, blank=True, null=True)
    checked_out_by = models.CharField(max_length=200, blank=True, null=True)

    def add(self):
        self.added_date = timezone.now()
        self.added_by = 'auth.User'
        self.save()

    def checkout(self):
        self.is_available = False
        self.checked_out_by = 'auth.User'
        self.save()

    def checkin(self):
        self.is_available = True
        self.checked_in_by = 'auth.User'
        self.save()

    def __str__(self):
        return self.name
