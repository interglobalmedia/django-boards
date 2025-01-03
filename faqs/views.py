from django.shortcuts import render
from django.http import HttpResponse
from .models import FAQ

# Create your views here.

def faqs_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs/faqs.html', {'faqs': faqs})
