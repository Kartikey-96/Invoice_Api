from django.db import models
import uuid

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    description = models.TextField()
    rate = models.DecimalField(decimal_places=2, max_digits=10, default=1)
    quantity = models.IntegerField(default=1)
    invoiceID = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE,)