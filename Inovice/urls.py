from django.urls import path
from .views import InvoiceView, InvoiceItemView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", InvoiceView.as_view(), name="all_invoices"),
    path("addinvoice", csrf_exempt(InvoiceView.as_view()), name="add_invoice"),
    path("editinvoice/<uuid:id>", csrf_exempt(InvoiceView.as_view()), name="edit_invoice"),
    path("deleteinvoice/<uuid:id>", csrf_exempt(InvoiceView.as_view()), name="delete_invoice"),
    
    path("<uuid:invoice_id>/items", csrf_exempt(InvoiceItemView.as_view()), name="invoice_items"),
]
