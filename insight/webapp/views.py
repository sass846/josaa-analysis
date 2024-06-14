from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def institutes(request):
    return render(request, 'webapp/institutes.html')

def seats(request):
    return render(request, 'webapp/seats.html')

def analysis(request):
    return render(request, 'webapp/analysis.html')