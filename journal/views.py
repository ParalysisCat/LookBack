from django.shortcuts import render
#from .models import JournalEntry  # We'll create this model next

def home(request):
    # For now, just render the template - we'll add random entry logic later
    return render(request, 'index.html')  # Matches your HTML filename