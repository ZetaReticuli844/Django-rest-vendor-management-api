from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import PurchaseOrder, HistoricalPerformance
from django.db.models import Avg, F, Count

@receiver([post_save, post_delete], sender=PurchaseOrder)
def update_historical_metrics(sender, instance, **kwargs):
    vendor = instance.vendor if hasattr(instance, 'vendor') else instance
    total_completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    # On-Time Delivery Rate Calculation
    on_time_completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=timezone.now()).count()
    on_time_delivery_rate = on_time_completed_pos / total_completed_pos if total_completed_pos > 0 else 0
    
    # Quality Rating Average
    quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False).aggregate(quality_rating_avg=Avg('quality_rating'))['quality_rating_avg'] or 0
    
    # Average Response Time
    average_response_time = completed_pos.aggregate(avg_response=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response']
    average_response_time=average_response_time.days
    
    # Fulfillment Rate
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfillment_rate = 0 if total_orders == 0 else PurchaseOrder.objects.filter(vendor=vendor, status='completed', issue_date__isnull=False).count() / total_orders

    # Update Historical Metrics
    HistoricalPerformance.objects.update_or_create(vendor=vendor,
                                                   defaults={
                                                       'date':timezone.now(),
                                                       'on_time_delivery_rate': on_time_delivery_rate,
                                                       'quality_rating_avg': quality_rating_avg,
                                                       'average_response_time': average_response_time,
                                                       'fulfillment_rate': fulfillment_rate
                                                   })
    
    

