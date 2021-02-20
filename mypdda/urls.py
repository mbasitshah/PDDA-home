from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name='Home'),
    path('results', views.results, name='Result'),
    path('SavedResults', views.savedresults, name='Saved'),
    path('gallery', views.gallery, name='Gallery'),
    path('Diseases', views.diseases, name='Diseases'),
    path('About', views.about, name='Home'),
    path('Help', views.help, name='Home'),
}
