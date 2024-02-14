from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"menu/index.html",context={})

def registration(request):
    return render(request,"menu/reistration.html",context={})