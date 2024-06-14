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
    paginator = Paginator(institutes, 15)
    page = request.GET.get('page')
    insti = paginator.get_page(page)
    start = (insti.number - 1) * insti.paginator.per_page
    nums = "a"*insti.paginator.num_pages
    return render(request, 'webapp/institutes.html', {
        'institutes': insti,
        'start': start,
        'nums': nums
        })

def seats(request):
    return render(request, 'webapp/seats.html')

def analysis(request):
    josaa_data = josaa.objects.all()
    return render(request, 'webapp/analysis.html', {'josaa': josaa_data})