from django.shortcuts import render
from .models import Home  # Import the Home model

def home(request):
    # Retrieve the Home object from the database (assuming there is only one)
    home = Home.objects.first()  # Assuming there is only one Home object
    context = {
        "home": home  # Pass the Home object to the template context
    }
    return render(request, "pages/home.html", context)
