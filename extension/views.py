from django.shortcuts import render

# Create your views here.

def extension_master(request):
    return render(request,'extension/master.html')

def extension_home(request):
    return render(request,'extension/home.html')

def extension_about(request):
    return render(request,'extension/about.html')

def extension_contact(request):
    return render(request,'extension/contact.html')

