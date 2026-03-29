from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def nutrients(request):
    return render(request, 'nutrients.html')

def contact(request):
    return render(request, 'contact.html')