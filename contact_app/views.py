from django.shortcuts import render, redirect
from .models import Contact
import re   

def home(request):
    return render(request, 'index.html')

def nutrients(request):
    return render(request, 'nutrients.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        errors = {}

        if not name:
            errors['name'] = 'Name is required'

        if not email:
            errors['email'] = 'Email is required'
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors['email'] = 'Enter a valid email'

        if not message:
            errors['message'] = 'Message is required'

        if errors:
            return render(request, 'contact.html', {
                'errors': errors,
                'name': name,
                'email': email,
                'message': message
            })

        Contact.objects.create(name=name, email=email, message=message)

        return render(request, 'contact.html', {
            'success': 'Your message has been sent!'
        })

    return render(request, 'contact.html')