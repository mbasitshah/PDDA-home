from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def results(request):
    return render(request, 'results.html')


def savedresults(request):
    return render(request, 'SavedResults.html')


def gallery(request):
    return render(request, 'gallery.html')


def diseases(request):
    return render(request, 'Diseases.html')


def help(request):
    return render(request, 'Help.html')


def about(request):
    return render(request, 'About.html')
