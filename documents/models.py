from django.db import models
import uuid

class Document(models.Model):
    DOC_TYPES = [
        ('invoice', 'Invoice'),
        ('receipt', 'Receipt'),
        ('contract', 'Contract'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending Processing'),
        ('processing', 'Extracting Data'),
        ('completed', 'Extracted'),
        ('failed', 'Extraction Error'),
    ]

    VERIFICATION_CHOICES = [
        ('unverified', 'Unverified'),
        ('passed', 'Kane Verified (Pass)'),
        ('failed', 'Verification Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    doc_type = models.CharField(max_length=50, choices=DOC_TYPES, default='invoice')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    
    # Extracted fields
    vendor_name = models.CharField(max_length=255, blank=True)
    invoice_number = models.CharField(max_length=100, blank=True)
    invoice_date = models.CharField(max_length=50, blank=True)
    currency = models.CharField(max_length=10, default='₦')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    line_items = models.JSONField(default=list, blank=True)
    raw_text = models.TextField(blank=True)
    
    # Verification metadata
    verification_status = models.CharField(max_length=50, choices=VERIFICATION_CHOICES, default='unverified')
    verification_notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.doc_type.upper()}: {self.vendor_name or 'Unknown'} ({self.formatted_total})"

    @property
    def formatted_total(self):
        if self.total_amount is not None:
            return f"{self.currency}{self.total_amount:,.2f}"
        return f"{self.currency}0.00"
