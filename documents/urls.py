from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_document, name='upload_document'),
    path('mock-invoice/', views.load_mock_invoice, name='load_mock_invoice'),
    path('toggle-bug/', views.toggle_bug, name='toggle_bug'),
    path('document/<uuid:doc_id>/', views.document_detail, name='document_detail'),
    path('api/document/<uuid:doc_id>/', views.api_document, name='api_document'),
]
