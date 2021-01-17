from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'gallery_UI_04.html')