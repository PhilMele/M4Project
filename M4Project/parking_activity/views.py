from django.shortcuts import render

# Create your views here.
def enter(request):
    return render(request, 'stays/enter.html')