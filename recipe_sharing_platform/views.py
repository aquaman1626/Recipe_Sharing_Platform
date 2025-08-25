from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Make sure to create a template 'home.html'
