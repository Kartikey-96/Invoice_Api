from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
import json
from .serializer import InvoiceSerializer, InvoiceItemSerializer
from .models import Invoice, InvoiceItem
import uuid

tem_Store = []

class InvoiceView(View):
    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        userData = json.loads(request.body)
        serializer = InvoiceSerializer(data=userData)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    def put(self, request, id):
        userData = json.loads(request.body)
        invoice = Invoice.objects.filter(id=id).first()
        print(invoice)
        if not invoice:
            return HttpResponseBadRequest("Invoice not found")

        serializer = InvoiceSerializer(invoice, data=userData, partial=True)
        if serializer.is_valid():
            serializer.save()
            tem_Store.append(serializer.data)
            print(tem_Store)
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    
    def delete(self, request, id):
        for index, item in enumerate(tem_Store):
            if item["id"] == str(id):
                tem_Store.remove(item)
                return JsonResponse({"message": "Invoice deleted successfully"}, status=200)
        return HttpResponseBadRequest("Invoice not found")


class InvoiceItemView(View):
    def get(self, request, invoice_id):
        # imoviceItem = InvoiceItem.objects.all()
        invoice = InvoiceItem.objects.filter(invoiceID=uuid.UUID(str(invoice_id)))
        if not invoice:
            return HttpResponseBadRequest("Invoice not found")

        # items = invoice.items.all()

        
        serializer = InvoiceItemSerializer(invoice, many=True)
       
        return JsonResponse({"data":serializer.data, "safe":False, "msg":"for getting data"})
    
    def post(self, request, invoice_id):
        invoice = Invoice.objects.filter(id=invoice_id).first()
        if not invoice:
            return HttpResponseBadRequest("Invoice not found")

        data = json.loads(request.body)
        serializer = InvoiceItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save(invoiceID=invoice)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
