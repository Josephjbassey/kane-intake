from django.test import TestCase, Client
from django.urls import reverse
from documents.models import Document

class DocumentIntakeTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Document Digitization Intake Agent")
        self.assertContains(response, "Verified with Kane CLI")

    def test_load_mock_invoice_successful_extraction(self):
        response = self.client.post(reverse('load_mock_invoice'), HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "₦12,500.00")
        self.assertContains(response, "Lagos Freight &amp; Logistics Ltd")
        self.assertContains(response, "INV-2026-1113")

        doc = Document.objects.first()
        self.assertIsNotNone(doc)
        self.assertEqual(doc.total_amount, 12500.00)
        self.assertEqual(doc.vendor_name, "Lagos Freight & Logistics Ltd")

    def test_planted_bug_mode_caught(self):
        # When simulate_bug is passed, total is ₦1,250.00 instead of ₦12,500.00
        response = self.client.post(reverse('load_mock_invoice'), {'simulate_bug': 'true'}, HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "₦1,250.00")
        self.assertContains(response, "00/00/2026")
        
        doc = Document.objects.first()
        self.assertEqual(doc.total_amount, 1250.00)
        self.assertEqual(doc.invoice_date, "00/00/2026")
