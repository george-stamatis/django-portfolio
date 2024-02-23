# pages/views.py

from django.shortcuts import render
from pages.models import Home

def home(request):
    image = Home.objects.all()
    context = {
        "image": image
    }
    return render(request, "pages/home.html", context)