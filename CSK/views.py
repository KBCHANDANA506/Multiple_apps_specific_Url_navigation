from django.shortcuts import render

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')

def jadeja(request):
    return render(request,'jadeja.html')