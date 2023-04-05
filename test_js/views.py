from django.shortcuts import render

# Create your views here.

def test_todo(request):
    return render(request,'test/todo.html')