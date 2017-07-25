from django.shortcuts import render, redirect

from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    for error in results['errors']:
        messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['loginMsg']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['userId'] = results['user'][0].id
        return redirect('/home')

