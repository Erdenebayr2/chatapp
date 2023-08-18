from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'mychatapp/index.html', context)

def userlog(request):
    return render(request, 'login.html')

def google_login(request):
    return render(request, 'google.html')