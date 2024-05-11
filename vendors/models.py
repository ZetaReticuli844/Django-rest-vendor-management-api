from django.db import models
from django.db import models
from django.core.validators import MinValueValidator

class Vendor(models.Model):
  name = models.CharField(max_length=255)
  contact_details = models.TextField()
  address = models.TextField()
  vendor_code = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

class PurchaseOrder(models.Model):
  po_number = models.CharField(max_length=50, unique=True)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  order_date = models.DateTimeField()
  delivery_date = models.DateTimeField(blank=True, null=True)
  items = models.JSONField()
  quantity = models.PositiveIntegerField()
  STATUS_CHOICES = (
      ('pending', 'Pending'),
      ('completed', 'Completed'),
      ('canceled', 'Canceled'),
  )
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  quality_rating = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0, "Rating cannot be negative")])
  issue_date = models.DateTimeField()
  acknowledgment_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return f"PO number: {self.po_number} - Vendor: {self.vendor}"

class HistoricalPerformance(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  date = models.DateField()
  on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0, "Rate cannot be negative")])
  quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0, "Rating cannot be negative")])
  average_response_time = models.FloatField(validators=[MinValueValidator(0.0, "Time cannot be negative")])
  fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0, "Rate cannot be negative")])

  def __str__(self):
    return f"Performance for {self.vendor} on {self.date}"
