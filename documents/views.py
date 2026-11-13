from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Document
from .services import extract_document_data, PLANTED_BUG_ACTIVE

def index(request):
    documents = Document.objects.all()[:10]
    latest_doc = Document.objects.first()
    context = {
        'documents': documents,
        'latest_doc': latest_doc,
        'planted_bug_active': PLANTED_BUG_ACTIVE,
    }
    return render(request, 'documents/index.html', context)

@csrf_exempt
@require_POST
def upload_document(request):
    uploaded_file = request.FILES.get('file')
    simulate_bug = request.POST.get('simulate_bug') == 'true'

    if not uploaded_file:
        return HttpResponse('<div class="rounded-xl border border-amber-200 bg-amber-50 p-4 text-xs font-medium text-amber-800">Please select a valid invoice PDF or image file first.</div>')

    # File size validation (10MB limit per security build rules)
    if uploaded_file.size > 10 * 1024 * 1024:
        return HttpResponse('<div class="rounded-xl border border-red-200 bg-red-50 p-4 text-xs font-medium text-red-800">File exceeds the 10MB limit.</div>')

    doc = Document.objects.create(
        title=uploaded_file.name,
        file=uploaded_file,
        status='processing'
    )
    extract_document_data(doc, simulate_bug=simulate_bug)

    if request.headers.get('HX-Request'):
        return render(request, 'documents/partials/extraction_card.html', {'doc': doc})
    return redirect('index')

@csrf_exempt
@require_POST
def load_mock_invoice(request):
    simulate_bug = request.POST.get('simulate_bug') == 'true'
    doc = Document.objects.create(
        title="Lagos_Logistics_Invoice_1113.pdf",
        doc_type="invoice",
        status="processing"
    )
    extract_document_data(doc, simulate_bug=simulate_bug)
    
    if request.headers.get('HX-Request'):
        return render(request, 'documents/partials/extraction_result.html', {'doc': doc, 'documents': Document.objects.all()[:10]})
    return redirect('index')

@require_POST
def toggle_bug(request):
    import documents.services as services
    services.PLANTED_BUG_ACTIVE = not services.PLANTED_BUG_ACTIVE
    return JsonResponse({'planted_bug_active': services.PLANTED_BUG_ACTIVE})

def document_detail(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'documents/partials/extraction_card.html', {'doc': doc})

def api_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return JsonResponse({
        'id': str(doc.id),
        'title': doc.title,
        'vendor_name': doc.vendor_name,
        'invoice_number': doc.invoice_number,
        'invoice_date': doc.invoice_date,
        'currency': doc.currency,
        'total_amount': str(doc.total_amount) if doc.total_amount else '0.00',
        'status': doc.status,
        'verification_status': doc.verification_status,
    })
