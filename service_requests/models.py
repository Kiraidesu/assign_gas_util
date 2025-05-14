from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class ServiceRequest(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    REQUEST_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('installation', 'New Installation'),
        ('billing', 'Billing Issue'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.status}"
