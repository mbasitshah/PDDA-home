from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'PDDA_Homescreen_UI_01.html')
