from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'create.html')

def about(request):
    return render(request,'index.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    return render(request,'contact.html')