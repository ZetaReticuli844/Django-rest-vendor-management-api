from rest_framework import serializers

from vendors.models import Vendor,PurchaseOrder,HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = PurchaseOrder
    fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
