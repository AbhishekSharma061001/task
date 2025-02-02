from django.urls import path
from faq import views
from . import views

urlpatterns = [
    path('faqs/', views.getFaqs, name='get_faqs'),
    path('translate/', views.translate_view, name='translate_view'),
]
