from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Institute, josaa

def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def institutes(request):
    institutes = Institute.objects.all()
    paginator = Paginator(institutes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webapp/institutes.html', {'page_obj': page_obj})

def seats(request):
    return render(request, 'webapp/seats.html')

def analysis(request):
    josaa_data = josaa.objects.all()
    return render(request, 'webapp/analysis.html', {'josaa': josaa_data})