from django.shortcuts import render
from django.core.paginator import Paginator
# from django.core import serializers
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
    institutes = josaa.objects.values_list('institute', flat=True).distinct()

    # institute_type = request.GET.get('institute_type')
    # if institute_type:
    #     josaa_data = josaa_data.filter(institute_type=institute_type)

    institute_name = request.GET.get('institute_name')
    if institute_name:
        josaa_data = josaa_data.filter(institute=institute_name)

    category = request.GET.get('category')
    if category:
        josaa_data = josaa_data.filter(category=category)

    gender = request.GET.get('gender')
    if gender:
        josaa_data = josaa_data.filter(gender=gender)

    paginator = Paginator(josaa_data, 10)
    page = request.GET.get('page')
    pg_data = paginator.get_page(page)
    start = (pg_data.number - 1) * pg_data.paginator.per_page
    nums = "a"*pg_data.paginator.num_pages


    # serialized_data = serializers.serialize('json', josaa_data)
    return render(request, 'webapp/analysis.html', {
        'institutes':institutes,
          'pg_data': pg_data,
          'start': start,
          'nums':nums
          })