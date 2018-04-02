from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def authenticateUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('getAllBooks'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('getAllBooks'))
        else:
            messages.error(request, 'password or username incorrect')
            return HttpResponseRedirect(reverse('authenticateUser'))
    return render(request, 'authenticate/login.html')

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('authenticateUser'))
    
