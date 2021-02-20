from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Results)

admin.site.register(Plants)
admin.site.register(Diseases)