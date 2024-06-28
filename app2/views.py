from django.shortcuts import render

# Create your views here.
def hPage(request):
    return render(request,'done.html')