"""
Document extraction and AI parsing services.
Includes mock parser with concrete test fixtures (₦12,500 mock invoice)
and support for closed-loop coding-agent repair verification.
"""

from decimal import Decimal
import re

# Closed-loop demonstration toggle
# When True, simulates a planted bug (e.g. missing zero or misparsed date) that Kane CLI detects.
# The coding agent loop detects the failure in Kane test output, patches this service, and re-verifies.
PLANTED_BUG_ACTIVE = False

MOCK_INVOICE_DATA = {
    "vendor_name": "Lagos Freight & Logistics Ltd",
    "invoice_number": "INV-2026-1113",
    "invoice_date": "13 Nov 2026",
    "currency": "₦",
    "total_amount": Decimal("12500.00"),
    "line_items": [
        {"description": "Inter-State Freight Haulage", "quantity": 1, "unit_price": "8,500.00", "total": "8,500.00"},
        {"description": "Secure Pallet Warehousing & Handling", "quantity": 1, "unit_price": "4,000.00", "total": "4,000.00"},
    ],
    "raw_text": "INVOICE\\nVendor: Lagos Freight & Logistics Ltd\\nInvoice #: INV-2026-1113\\nDate: 13 Nov 2026\\nTotal: ₦12,500.00"
}

def extract_document_data(document, simulate_bug=False):
    """
    Extracts structured data from an uploaded document.
    Falls back to deterministic mock invoice values for automated testing.
    """
    use_bug = simulate_bug or PLANTED_BUG_ACTIVE

    if document.file:
        filename = document.file.name.lower()
    else:
        filename = "mock_invoice.pdf"

    # Default extraction based on mock invoice
    vendor = MOCK_INVOICE_DATA["vendor_name"]
    inv_num = MOCK_INVOICE_DATA["invoice_number"]
    inv_date = MOCK_INVOICE_DATA["invoice_date"]
    currency = MOCK_INVOICE_DATA["currency"]
    total = MOCK_INVOICE_DATA["total_amount"]
    items = list(MOCK_INVOICE_DATA["line_items"])

    if use_bug:
        # Planted bug: decimal misread causing ₦1,250.00 instead of ₦12,500.00
        # Kane objective "verify the total shows ₦12,500" will catch this!
        total = Decimal("1250.00")
        inv_date = "00/00/2026"

    document.vendor_name = vendor
    document.invoice_number = inv_num
    document.invoice_date = inv_date
    document.currency = currency
    document.total_amount = total
    document.line_items = items
    document.raw_text = MOCK_INVOICE_DATA["raw_text"]
    document.status = 'completed'
    document.save()

    return document
