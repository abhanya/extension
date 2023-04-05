from django.shortcuts import render

# Create your views here.

def cake_main(request):
    return render(request,'pages/cakes.html')

def cake_home(request):
    return render(request,'pages/home.html')

def cake_cont(request):
    return render(request,'pages/cnt.html')

def cake_abt(request):
    return render(request,'pages/aboutus.html')

def cake_desert(request):
    return render(request,'pages/deserts.html')

def cake_graduation(request):
    return render(request,'pages/graduationcakes.html')

def cake_snacks(request):
    return render(request,'pages/snacks.html')
