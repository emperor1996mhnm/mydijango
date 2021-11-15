from django.shortcuts import render
from django.shortcuts import HttpResponse
def about(request):
    #return HttpResponse("print(5555*555)")
    return render(request , 'about.html')
def home(request):
    #return HttpResponse('home')
        return render(request , 'Home.html')
