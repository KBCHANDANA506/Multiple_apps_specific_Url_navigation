from django.shortcuts import render

# Create your views here.
def pandya(request):
    return render(request,'pandya.html')

def rohit(request):
    return render(request,'rohit.html')