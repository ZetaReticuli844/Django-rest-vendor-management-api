from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from vendors.models import Vendor, PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer,VendorPerformanceSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone

class VendorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Vendor.objects.all()
        serializer = VendorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Vendor.objects.all()
        vendor = get_object_or_404(queryset, pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def update(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PurchaseOrderViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = PurchaseOrder.objects.all()
        purchase_order = get_object_or_404(queryset, pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class VendorPerformanceViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = HistoricalPerformance.objects.all()
        vendor_performance = get_object_or_404(queryset, vendor=pk)
        serializer = VendorPerformanceSerializer(vendor_performance)
        return Response(serializer.data)
 
 
